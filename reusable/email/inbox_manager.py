import requests
from typing import Any, Dict, Optional, Union
import json
from . import crypto
from .errors import *
from .types import Inbox, Email
import aiohttp


# API Version Constant
INTERNAL_API_VERSION = 1

# Utility Class for JSON Handling
class Utils:
  """Utility methods for handling JSON operations."""

  @staticmethod
  def handle_metadata(obj: Any) -> dict:
    """Convert an object to a JSON-serializable dictionary."""
    try:
      return dict(obj)
    except Exception:
      raise TypeError(f"Type {obj.__class__.__name__} is not JSON serializable")

  @staticmethod
  def to_json(obj: Any) -> str:
    """Convert an object to a JSON string."""
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=True, default=Utils.handle_metadata)

  from_json = staticmethod(json.loads)  # Parse JSON string to Python object

# Route Class for API Requests
class Route:
  """Represents an API route."""

  def __init__(self, base: str, method: str, path: str) -> None:
    self.BASE = base
    self.path = path
    self.method = method
    self.url = f"{self.BASE}{self.path}"

# Synchronous API Session Handler
class Sync:
  """Manages a synchronized session with the API."""

  def __init__(self, authorization: str, private_key: Optional[bytes] = None) -> None:
    self.private_key = private_key.decode('utf-8') if private_key else None
    self.session: Optional[requests.Session] = None
    self.BASE_URL = f"http://api.reusable.email/v{INTERNAL_API_VERSION}"
    self.generate_session(authorization)

  def generate_session(self, authorization: str) -> None:
    """Initialize the API session with the necessary headers."""
    self.session = requests.Session()
    self.session.headers.update({
      'User-Agent': 'Python-SDK-Package/1.0',
      'Authorization': authorization
    })

  @staticmethod
  def json_or_text(response: requests.Response) -> Union[Dict[str, Any], str]:
    """Extract JSON or text response from an HTTP response."""
    text = response.text
    try:
      if response.headers.get('Content-Type', '').startswith('application/json'):
        return Utils.from_json(text)
    except KeyError:
      pass
    return text

  def request(self, route: Route, headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> requests.Response:
    """Send an HTTP request based on the given route and parameters."""
    methods = {
      'get': self.session.get,
      'post': self.session.post,
      'put': self.session.put,
      'delete': self.session.delete
    }

    if route.method not in methods:
      raise ValueError(f"Unsupported HTTP method: {route.method}")

    with methods[route.method](route.url, headers=headers, params=params, json=json, data=data) as response:
      data = self.json_or_text(response)
      if response.status_code in {200, 202}:
        return response
      elif response.status_code == 403:
        raise Forbidden(response, data)
      elif response.status_code == 404:
        raise NotFound(response, data)
      elif response.status_code == 400:
        raise InvalidParams(response, data)
      elif response.status_code >= 500:
        raise FetchFail(response, data)
      elif response.status_code >= 401:
        raise HTTPException(response, data)
      else:
        raise HTTPException(response, data)

  # Reg Inboxes
  def view_inbox(self, alias: str, after: Optional[str] = None) -> Union[Inbox, requests.Response]:
    """View the content of an inbox."""
    params = {"alias": alias}
    if after:
      params["after"] = after
    response = self.request(route=Route(self.BASE_URL, 'get', "/inbox"), params=params)
    if response.status_code == 200:
      return response.json().get('inbox')
    return response

  def fetch_email_body(self, alias: str, email_id: str) -> Union[str, requests.Response]:
    """Fetch a specific email's body from the inbox."""
    params = {"alias": alias, "id": email_id}
    response = self.request(route=Route(self.BASE_URL, 'get', "/email"), params=params)
    if response.status_code == 200:
      return response.text
    return response

  def delete_email(self, alias: str, email_id: str) -> Union[bool, requests.Response]:
    """Delete a specific email from the inbox."""
    params = {"alias": alias, "id": email_id}
    response = self.request(route=Route(self.BASE_URL, 'delete', "/email"), params=params)
    if response.status_code == 200:
      return response.json().get('success', False)
    return response
      
  # Encrypted Inboxes
  def create_encrypted_inbox(self, alias: str, public_key: bytes) -> requests.Response:
    """Create a new encrypted inbox."""
    json_data = {"publicKey": public_key.decode('utf-8'), "inboxName": alias.upper()}
    return self.request(route=Route(self.BASE_URL, 'post', "/encrypted/inbox"), data=json_data)

  def view_encrypted_inbox(self, alias: str, after: Optional[str] = None) -> Union[Inbox, requests.Response]:
    """View the content of an inbox."""
    params = {"alias": alias.upper()}
    if after:
      params["after"] = after
    response = self.request(route=Route(self.BASE_URL, 'get', "/encrypted/inbox"), params=params)
    if response.status_code == 200 and self.private_key:
      inbox: Inbox = []
      for email in response.json().get('inbox', []):
        decrypted_email = crypto.decrypt_email(email, self.private_key)
        inbox.append(decrypted_email)
      return inbox
    return response.json()

  def fetch_encrypted_email(self, alias: str, email_id: str) -> Union[Email, requests.Response]:
    """Fetch a specific email from the inbox."""
    params = {"alias": alias.upper(), "id": email_id}
    response = self.request(route=Route(self.BASE_URL, 'get', "/encrypted/email"), params=params)
    if response.status_code == 200 and self.private_key:
      return crypto.decrypt_email(response.json(), self.private_key)
    return response.json()

  def delete_encrypted_email(self, alias: str, email_id: str) -> Union[bool, requests.Response]:
    """Delete a specific email from the inbox."""
    params = {"alias": alias.upper(), "id": email_id}
    response = self.request(route=Route(self.BASE_URL, 'delete', "/encrypted/email"), params=params)
    if response.status_code == 200:
      return response.json().get('success', False)
    return response
      
class Async:
  """Manages an asynchronous session with the API."""

  def __init__(self, authorization: str, private_key: Optional[bytes] = None) -> None:
    self.private_key = private_key.decode('utf-8') if private_key else None
    self.session: Optional[aiohttp.ClientSession] = None
    self.BASE_URL = f"http://api.reusable.email/v{INTERNAL_API_VERSION}"
    self.authorization = authorization

  async def generate_session(self) -> None:
    """Initialize the API session with the necessary headers."""
    self.session = aiohttp.ClientSession(
      headers={
        'User-Agent': 'Python-SDK-Package/1.0',
        'Authorization': self.authorization,
      }
    )

  @staticmethod
  async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    """Extract JSON or text response from an HTTP response."""
    text = await response.text()
    try:
      if response.headers.get('Content-Type', '').startswith('application/json'):
        return await response.json()
    except KeyError:
      pass
    return text

  async def request(
    self, route: Route, headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None
  ) -> aiohttp.ClientResponse:
    """Send an asynchronous HTTP request based on the given route and parameters."""
    if not self.session:
      await self.generate_session()

    methods = {
      'get': self.session.get,
      'post': self.session.post,
      'put': self.session.put,
      'delete': self.session.delete
    }

    if route.method not in methods:
      raise ValueError(f"Unsupported HTTP method: {route.method}")

    async with methods[route.method](
      route.url, headers=headers, params=params, json=json
    ) as response:
      data = await self.json_or_text(response)
      if response.status in {200, 202}:
        return response
      elif response.status == 403:
        raise Forbidden(response, data)
      elif response.status == 404:
        raise NotFound(response, data)
      elif response.status == 400:
        raise InvalidParams(response, data)
      elif response.status >= 500:
        raise FetchFail(response, data)
      elif response.status >= 401:
        raise HTTPException(response, data)
      else:
        raise HTTPException(response, data)

  async def view_inbox(self, alias: str, after: Optional[str] = None) -> Union[Inbox, aiohttp.ClientResponse]:
    """View the content of an inbox."""
    params = {"alias": alias}
    if after:
      params["after"] = after
    response = await self.request(route=Route(self.BASE_URL, 'get', "/inbox"), params=params)
    if response.status == 200:
      return await response.json().get('inbox')
    return response

  async def fetch_email_body(self, alias: str, email_id: str) -> Union[str, aiohttp.ClientResponse]:
    """Fetch a specific email from the inbox."""
    params = {"alias": alias, "id": email_id}
    response = await self.request(route=Route(self.BASE_URL, 'get', "/email"), params=params)
    if response.status == 200:
      return await response.text('utf-8')
    return response

  async def delete_email(self, alias: str, email_id: str) -> Union[bool, aiohttp.ClientResponse]:
    """Delete a specific email from the inbox."""
    params = {"alias": alias, "id": email_id}
    response = await self.request(route=Route(self.BASE_URL, 'delete', "/email"), params=params)
    if response.status == 200:
      return (await response.json()).get('success', False)
    return response


  async def create_encrypted_inbox(self, alias: str, public_key: bytes) -> aiohttp.ClientResponse:
    """Create a new encrypted inbox."""
    json_data = {"publicKey": public_key.decode('utf-8'), "inboxName": alias.upper()}
    return await self.request(route=Route(self.BASE_URL, 'post', "/encrypted/inbox"), json=json_data)

  async def view_encrypted_inbox(self, alias: str, after: Optional[str] = None) -> Union[Inbox, aiohttp.ClientResponse]:
    """View the content of an inbox."""
    params = {"alias": alias.upper()}
    if after:
      params["after"] = after
    response = await self.request(route=Route(self.BASE_URL, 'get', "/encrypted/inbox"), params=params)
    
    if response.status == 200 and self.private_key:
      inbox: Inbox = []
      json_response = await response.json()
      for email in json_response.get('inbox', []):
        decrypted_email = crypto.decrypt_email(email, self.private_key)
        inbox.append(decrypted_email)
      return inbox
    return await response.json()
  
  async def fetch_encrypted_email(self, alias: str, email_id: str) -> Union[Email, aiohttp.ClientResponse]:
    """Fetch a specific email from the inbox."""
    params = {"alias": alias.upper(), "id": email_id}
    response = await self.request(route=Route(self.BASE_URL, 'get', "/encrypted/email"), params=params)
    
    if response.status == 200 and self.private_key:
      json_response = await response.json()
      return crypto.decrypt_email(json_response, self.private_key)
    return await response.json()

  async def delete_encrypted_email(self, alias: str, email_id: str) -> Union[bool, aiohttp.ClientResponse]:
    """Delete a specific email from the inbox."""
    params = {"alias": alias.upper(), "id": email_id}
    response = await self.request(route=Route(self.BASE_URL, 'delete', "/encrypted/email"), params=params)
    
    if response.status == 200:
      json_response = await response.json()
      return json_response.get('success', False)
    return response

  async def close(self) -> None:
    """Close the session."""
    if self.session:
      await self.session.close()
    
    
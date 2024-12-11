from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import TypeGuard
from .error import (
  Error as ErrorPayload,
  FormErrors as FormErrorsPayload,
  FormErrorWrapper as FormErrorWrapperPayload,
)


def _flatten_error_dict(d: FormErrorsPayload, key: str = '') -> Dict[str, str]:
  """
  Flattens a nested dictionary of form errors into a single-level dictionary.

  Args:
    d (FormErrorsPayload): The form errors payload to flatten.
    key (str, optional): The parent key for nested dictionary keys. Defaults to ''.

  Returns:
    Dict[str, str]: Flattened dictionary of errors.
  """

  def is_wrapper(x: FormErrorsPayload) -> TypeGuard[FormErrorWrapperPayload]:
    """Checks if a dictionary is a FormErrorWrapper."""
    return '_errors' in x

  items: List[Tuple[str, str]] = []

  # Handle miscellaneous errors
  if is_wrapper(d) and not key:
    items.append(('miscellaneous', ' '.join(x.get('message', '') for x in d['_errors'])))
    d.pop('_errors', None)  # type: ignore

  # Iterate over dictionary items
  for k, v in d.items():
    new_key = f"{key}.{k}" if key else k

    if isinstance(v, dict):
      if is_wrapper(v):
        _errors = v['_errors']
        items.append((new_key, ' '.join(x.get('message', '') for x in _errors)))
      else:
        items.extend(_flatten_error_dict(v, new_key).items())
    else:
      items.append((new_key, str(v)))  # type: ignore

  return dict(items)


class HTTPException(Exception):
  """Base exception for HTTP-related errors."""

  def __init__(self, response: Any, message: Optional[Union[str, Dict[str, Any]]]):
    self.response = response
    self.code: int = 0
    self.text: str = ""
    self.json: ErrorPayload
    self.payment_id: Optional[int] = None

    if isinstance(message, dict):
      self.json = message  # type: ignore
      self.code = message.get('code', 0)
      base = message.get('message', '')
      errors = message.get('errors')
      if errors:
        errors = _flatten_error_dict(errors)
        helpful = '\n'.join(f"In {k}: {v}" for k, v in errors.items())
        self.text = f"{base}\n{helpful}"
      else:
        self.text = base
    else:
      self.text = message or ''
      self.json = {'code': 0, 'message': message or ''}

    try: # TODO Update this for sync/async
      fmt = f'{response.status} {response.reason} (error code: {self.code})'
    except:
      fmt = f'{response.status_code} {response.reason} (error code: {self.code})'
    if self.text:
      fmt += f': {self.text}'
    super().__init__(fmt)


class RateLimited(Exception):
  """Raised for status code 429 with excessive timeout."""

  __slots__ = ('retry_after',)

  def __init__(self, retry_after: float):
    self.retry_after = retry_after
    super().__init__(f'Too many requests. Retry in {retry_after:.2f} seconds.')


class Forbidden(HTTPException):
  """Raised for status code 403."""

  __slots__ = ()


class NotFound(HTTPException):
  """Raised for status code 404."""

  __slots__ = ()


class FetchFail(HTTPException):
  """Raised for 500 range status codes."""

  __slots__ = ()


class InvalidParams(HTTPException):
  """Raised for status code 405."""

  __slots__ = ()

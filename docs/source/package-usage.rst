Package Documentation
=====================

.. _installation:

Installation
------------

To use `reusable.email`, first install it using pip:

.. code-block:: console

   (.venv) $ pip install reusable-email

Getting Started
---------------

`reusable.email` provides both synchronous and asynchronous classes for interacting with the API. Additionally, it includes a utility function for generating RSA public and private keys.

.. _synchronous-usage:

Synchronous Usage
~~~~~~~~~~~~~~~~~

The `Sync` class is used for synchronous operations:

.. code-block:: python

   from reusable.email import Sync

   # Initialize the Sync client
   sync_client = Sync(authorization="your-api-token")

   # View an inbox
   inbox = sync_client.view_inbox(alias="example_alias")
   print(inbox)

   # Fetch a specific email
   email = sync_client.fetch_email(alias="example_alias", email_id="email_id")
   print(email)

   # Delete an email
   success = sync_client.delete_email(alias="example_alias", email_id="email_id")
   print("Deleted successfully:", success)


Also in the `Sync` class is our encrypted inbox support:

.. _asynchronous-usage:

Asynchronous Usage
~~~~~~~~~~~~~~~~~~

The `Async` class is used for asynchronous operations with `aiohttp`:

.. code-block:: python

   import asyncio
   from reusable.email import Async

   async def main():
       # Initialize the Async client
       async_client = Async(authorization="your-api-token")

       # View an inbox
       inbox = await async_client.view_inbox(alias="example_alias")
       print(inbox)

       # Fetch a specific email
       email = await async_client.fetch_email(alias="example_alias", email_id="email_id")
       print(email)

       # Delete an email
       success = await async_client.delete_email(alias="example_alias", email_id="email_id")
       print("Deleted successfully:", success)

       # Close the session
       await async_client.close()

   asyncio.run(main())


.. _rsa-generation:

Generating RSA Keys
~~~~~~~~~~~~~~~~~~~

To get started with our encrypted inboxes generate your RSA keys, in our package we've made it easy to generate them.
Use `reusable.email.generate_keys` to easily generate RSA public and private keys in PEM format:

.. code-block:: python

   from reusable.email import generate_keys

   # Generate RSA keys
   public_key, private_key = generate_keys()

   print("Public Key:")
   print(public_key.decode("utf-8"))

   print("Private Key:")
   print(private_key.decode("utf-8"))


.. _encrypted-inbox:

Encrypted Inbox Support
~~~~~~~~~~~~~~~~~~~~~~~

Both `Sync` and `Async` classes provide methods for handling encrypted inboxes. Use the generated RSA keys to create or access encrypted inboxes.


.. code-block:: python

   from reusable.email import Sync, generate_keys

   # Generate byte strings of our private/public keys. We will use then later
   public_key, private_key = generate_keys()


   # Initialize the Sync client

   # Optionally you can exclude the bytes private key and decrypt manually
   # sync_client = Sync(authorization="your-api-token") 
   sync_client = Sync(authorization="your-api-token", private_key)
   
   # Generate a alias in the format of regular expression r'^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$'
   # EXAMPLES: A1B2-C3D4-E5F6, ABCD-1234-EFGH, 1234-5678-9012, 1234-ABCD-5678
   alias = lambda: '-'.join(
      ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) 
      for _ in range(3)
   )

   # Create our encrypted inbox. This will raise **InvalidParams** if alias is not in the right format
   inbox = sync_client.create_encrypted_inbox(alias, public_key)

   # View an inbox
   # If the private_key was defined this will return a decrypted inbox otherwise will return the http server response json
   inbox = sync_client.view_encrypted_inbox(alias=alias)
   print(inbox)

   # Fetch a specific email
   # If the private_key was defined this will return a decrypted inbox otherwise will return the http server response json
   email = sync_client.fetch_email(alias=alias, email_id="email_id")
   print(email)

   # Delete an email
   success = sync_client.delete_email(alias=alias, email_id="email_id")
   print("Deleted successfully:", success)

.. _error-handling:

Error Handling
--------------

The library includes error handling for common HTTP response statuses. Errors include:
- `Forbidden`: Raised when a 403 response is received.
- `NotFound`: Raised when a 404 response is received.
- `InvalidParams`: Raised when a 400 response is received.
- `FetchFail`: Raised for server-side errors (500+ status codes).
- `HTTPException`: Raised for all other HTTP errors.

.. code-block:: python

   from reusable.email import Sync

   try:
       sync_client = Sync(authorization="your-api-token")
       inbox = sync_client.view_inbox(alias="example_alias")
   except Forbidden:
       print("Access denied")
   except NotFound:
       print("Inbox not found")
   except Exception as e:
       print(f"An error occurred: {e}")

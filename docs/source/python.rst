Python Reference
=============================

Generating RSA Keys
-------------------
.. method:: reusable.email.generate_keys(public_exponent=65537, key_size=2048) -> tuple[bytes, bytes]
   
   Generate a pair of RSA public and private keys.
   
   :param public_exponent: Public exponent for the key generation. Default is ``65537``.
   :type public_exponent: int
   :param key_size: Size of the key in bits. Default is ``2048``.
   :type key_size: int
   :returns: A tuple containing the public key and private key in PEM format as bytes.
   :rtype: tuple[bytes, bytes]


Synchronous API
----------------

.. autoclass:: reusable.email.Sync
   :members:
   :undoc-members:
   :show-inheritance:  
   :noindex:

   Methods
   ~~~~~~~

   Session related methods
   -----------------------
   .. automethod:: reusable.email.Sync.generate_session
      
   
   General inboxes
   ---------------
   .. automethod:: reusable.email.Sync.view_inbox
   .. automethod:: reusable.email.Sync.fetch_email_body
   .. automethod:: reusable.email.Sync.delete_email

   Encrypted inboxes
   -----------------
   .. automethod:: reusable.email.Sync.create_encrypted_inbox
   .. automethod:: reusable.email.Sync.view_encrypted_inbox
   .. automethod:: reusable.email.Sync.fetch_encrypted_email
   .. automethod:: reusable.email.Sync.delete_encrypted_email


Asynchronous API
----------------

.. autoclass:: reusable.email.Async
  :members:
  :undoc-members:
  :show-inheritance:
  :noindex:

  Methods
  ~~~~~~~

  Session related methods
  -----------------------
  .. automethod:: reusable.email.Async.generate_session
   
  
  General inboxes
  ---------------
  .. automethod:: reusable.email.Async.view_inbox
  .. automethod:: reusable.email.Async.fetch_email_body
  .. automethod:: reusable.email.Async.delete_email

  Encrypted inboxes
  -----------------
  .. automethod:: reusable.email.Async.create_encrypted_inbox
  .. automethod:: reusable.email.Async.view_encrypted_inbox
  .. automethod:: reusable.email.Async.fetch_encrypted_email
  .. automethod:: reusable.email.Async.delete_encrypted_email


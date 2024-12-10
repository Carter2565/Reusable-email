
Asynchronous API
----------------

.. autoclass:: reusable.email.Async
  :members:
  :undoc-members:
  :show-inheritance:

  Methods
  ~~~~~~~

  Session related methods
  -----------------------
  .. automethod:: reusable.email.Async.generate_session
  
  General inboxes
  ---------------
  .. automethod:: reusable.email.Async.view_inbox
  .. automethod:: reusable.email.Async.fetch_email
  .. automethod:: reusable.email.Async.delete_email

  Encrypted inboxes
  -----------------
  .. automethod:: reusable.email.Async.create_encrypted_inbox
  .. automethod:: reusable.email.Async.view_encrypted_inbox
  .. automethod:: reusable.email.Async.fetch_encrypted_email
  .. automethod:: reusable.email.Async.delete_encrypted_email


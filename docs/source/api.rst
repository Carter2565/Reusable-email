API Reference
=============

.. toctree::
   :hidden:

   api/sync
   api/async

Synchronous API
---------------

.. autoclass:: reusable.email.Sync
   :members:
   :undoc-members:
   :show-inheritance:

   Methods
   ~~~~~~~
   .. automethod:: reusable.email.Sync.generate_session
   .. automethod:: reusable.email.Sync.view_inbox
   .. automethod:: reusable.email.Sync.fetch_email
   .. automethod:: reusable.email.Sync.delete_email
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

   Methods
   ~~~~~~~
   .. automethod:: reusable.email.Async.generate_session
   .. automethod:: reusable.email.Async.view_inbox
   .. automethod:: reusable.email.Async.fetch_email
   .. automethod:: reusable.email.Async.delete_email
   .. automethod:: reusable.email.Async.create_encrypted_inbox
   .. automethod:: reusable.email.Async.view_encrypted_inbox
   .. automethod:: reusable.email.Async.fetch_encrypted_email
   .. automethod:: reusable.email.Async.delete_encrypted_email

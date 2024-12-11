API Reference
=============

.. toctree::
   :hidden:

Reusable Email API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. module:: reusable_email
   :synopsis: Provides access to the Reusable Email API.

This document details the available API endpoints, their usage, and parameters.

Endpoints
---------

.. http:get:: /v1/inbox

   Fetches all emails in the specified inbox.

   **Parameters**

   - `alias` (string): The alias name of the inbox.

   **Example Request**

   .. code-block:: http

      GET /v1/inbox?alias=example_alias HTTP/1.1
      Host: api.reusable.email

   **Example Response**

   .. code-block:: json

      {
          "emails": [
              {"id": "123", "subject": "Welcome!", "timestamp": "2024-12-10T10:00:00Z"},
              {"id": "124", "subject": "Your account details", "timestamp": "2024-12-11T10:00:00Z"}
          ]
      }

.. http:get:: /v1/email

   Fetches the body of a specific email.

   **Parameters**

   - `alias` (string): The alias name of the inbox.
   - `id` (string): The email ID to fetch.

   **Example Request**

   .. code-block:: http

      GET /v1/email?alias=example_alias&id=123 HTTP/1.1
      Host: api.reusable.email

   **Example Response**

   .. code-block:: html

      '<div dir="ltr">This is and example body<br/></div>\n'

.. http:delete:: /v1/email

   Deletes a specific email from the inbox.

   **Parameters**

   - `alias` (string): The alias name of the inbox.
   - `id` (string): The email ID to delete.

   **Example Request**

   .. code-block:: http

      DELETE /v1/email?alias=example_alias&id=123 HTTP/1.1
      Host: api.reusable.email

   **Example Response**

   .. code-block:: json

      {
          "status": "success",
          "message": "Email deleted successfully."
      }

.. http:post:: /v1/encrypted/inbox

   Creates a new encrypted inbox.

   **Request Body**

   - `publicKey` (string): The public key encoded in UTF-8.
   - `inboxName` (string): The alias name in the format `^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$`.

   **Example Request**

   .. code-block:: http

      POST /v1/encrypted/inbox HTTP/1.1
      Host: api.reusable.email
      Content-Type: application/json

      {
          "publicKey": "MIIBIjANBgkqhki...",
          "inboxName": "ABCD-1234-EFGH"
      }

   **Example Response**

   .. code-block:: json

      {
          "status": "success",
          "inboxId": "encrypted_12345"
      }

.. http:get:: /v1/encrypted/inbox

   Fetches the details of an encrypted inbox.

   **Parameters**

   - `alias` (string): The alias name in the required format.

   **Example Request**

   .. code-block:: http

      GET /v1/encrypted/inbox?alias=ABCD-1234-EFGH HTTP/1.1
      Host: api.reusable.email

   **Example Response**

   .. code-block:: json

      {
          "inbox": {
              "alias": "ABCD-1234-EFGH",
              "emails": []
          }
      }

.. http:get:: /v1/encrypted/email

   Fetches the details of a specific encrypted email.

   **Parameters**

   - `alias` (string): The alias name in the required format.
   - `id` (string): The email ID to fetch.

   **Example Request**

   .. code-block:: http

      GET /v1/encrypted/email?alias=ABCD-1234-EFGH&id=123 HTTP/1.1
      Host: api.reusable.email

   **Example Response**

   .. code-block:: json

      {
          "id": "123",
          "subject": "Encrypted Email",
          "body": "This is an encrypted email body.",
          "timestamp": "2024-12-10T10:00:00Z"
      }

.. http:delete:: /v1/encrypted/email

   Deletes a specific encrypted email.

   **Parameters**

   - `alias` (string): The alias name in the required format.
   - `id` (string): The email ID to delete.

   **Example Request**

   .. code-block:: http

      DELETE /v1/encrypted/email?alias=ABCD-1234-EFGH&id=123 HTTP/1.1
      Host: api.reusable.email

   **Example Response**

   .. code-block:: json

      {
          "status": "success",
          "message": "Encrypted email deleted successfully."
      }

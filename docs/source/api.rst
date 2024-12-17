API Reference
=============

.. toctree::
   :hidden:

Reusable Email API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. module:: reusable_email
   :synopsis: Provides access to the Reusable Email API.

This document details the available API endpoints, their usage, and parameters.

**Headers**

.. code-block:: json

   {
      "Authorization": "Your_API_Key"
   }

Endpoints
---------

GET /v1/inbox
~~~~~~~~~~~~~

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
   "alias": "EXAMPLE",
   "inbox": [
      {
         "body": "Example Body\n",
         "headers": {
         "MIME": {"MIME":"MIME Related Info"},
         "SMTP": {"SMTP":"SMTP Related Info"}
      },
      "id": "861cbdb0b223ad18",
      "sender": "Carter <Carter@carter2565.dev>",
      "subject": "Example Title",
      "timestamp": 1734448240.0
      },
   ] 
   }

GET /v1/email
~~~~~~~~~~~~~

Fetches the body of a specific email.

**Parameters**

- `alias` (string): The alias name of the inbox.
- `id` (string): The email ID to fetch.

**Example Request**

.. code-block:: http

   GET /v1/email?alias=example&id=861cbdb0b223ad18 HTTP/1.1
   Host: api.reusable.email

**Example Response**

.. code-block:: html

   <div dir="ltr">Example Body<br/></div>

DELETE /v1/email
~~~~~~~~~~~~~~~~

Deletes a specific email from the inbox.

**Parameters**

- `alias` (string): The alias name of the inbox.
- `id` (string): The email ID to delete.

**Example Request**

.. code-block:: http

   DELETE /v1/email?alias=example&id=861cbdb0b223ad18 HTTP/1.1
   Host: api.reusable.email

**Example Response**

.. code-block:: json

   {
      "success": true
   }

POST /v1/encrypted/inbox
~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a new encrypted inbox.

**Request Body**

- `publicKey` (string): The public key encoded in UTF-8.
- `inboxName` (string): The alias name in the format `^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$`. See more in our :ref:Encrypted Inbox Management docs


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
      "message": "Inbox created successfully"
   }


GET /v1/encrypted/inbox
~~~~~~~~~~~~~~~~~~~~~~~

Fetches the details of an encrypted inbox.

**Parameters**

- `alias` (string): The alias name in the required format.

**Example Request**

.. code-block:: http

   GET /v1/encrypted/inbox?alias=R0WB-FNSC-NVLP HTTP/1.1
   Host: api.reusable.email

**Example Response**

.. code-block:: json

   {
      "alias": "R0WB-FNSC-NVLP",
      "inbox": [  
         {            
            "encrypted_aes_key": "mXZCi0eKaw/u+Az8CpMOaUDX/99g13jCLss/QYU64vpHr1yZstcdSKWyRR03IsTVstGVNnpDH2Xi05gJ7CpbTKQ0Fcy/brCjDSCgQtwPcJkJwBapWT+hTNoFWgerWtJMg02whhJLItuNwVb45k+ZKPDls7rvhawIeeLIyAxftLrOj3xXimpUv5C82I+rx3KspS029rWiTdqBvjJPq1I4HEiZdW5WHDGOf1erNop4I2enHzxZXw6HG75uh8OWWi+N7gl1TIWEF9BbwXJQ8/GgQyqsEBCRxoNFLmhvzy9BkyepAEYJOTTnjct3JRUAdMKBxV8FMfUa3ao9U01TLy90Ww==",
            "encrypted_email_data": "D0P5UaervsZOlgFYt5SQbygrUvLoaV/jQsX1e2snmuR7uNcc0o9EuGeO36SCmChOaT6FOnSf0v5vP2o6QBxr5Ov6z1VlEpopZjHBnnsMVJkdb09hSdplmW39D5/txdY9mXlg0UYyIGnzy57wvDTjkgGG2r/vRTz+MqR+N6Ck3/767k6n43qNe8/AMoDLJ9wwVWxiohai9+qRf2Se5+BS18JxPuum98vzE4gYhuK/oMvOYGTYkLk7cr+TzRGEtgMfmbjKpJf5gCOZ8fUXAjQc",
            "encrypted_iv": "vVLFgDcY0hJi1ylDX2sO8A==",
            "public_key": "PUBLIC_KEY",
            "timestamp": 1734451731
         }
      ]
   }

GET /v1/encrypted/email
~~~~~~~~~~~~~~~~~~~~~~~

Fetches the details of a specific encrypted email.

**Parameters**

- `alias` (string): The alias name in the required format.
- `id` (string): The email ID to fetch.

**Example Request**

.. code-block:: http

   GET /v1/encrypted/email?alias=R0WB-FNSC-NVLP&id=e3c83defb603f949 HTTP/1.1
   Host: api.reusable.email

**Example Response**

.. code-block:: json

   {            
      "encrypted_aes_key": "mXZCi0eKaw/u+Az8CpMOaUDX/99g13jCLss/QYU64vpHr1yZstcdSKWyRR03IsTVstGVNnpDH2Xi05gJ7CpbTKQ0Fcy/brCjDSCgQtwPcJkJwBapWT+hTNoFWgerWtJMg02whhJLItuNwVb45k+ZKPDls7rvhawIeeLIyAxftLrOj3xXimpUv5C82I+rx3KspS029rWiTdqBvjJPq1I4HEiZdW5WHDGOf1erNop4I2enHzxZXw6HG75uh8OWWi+N7gl1TIWEF9BbwXJQ8/GgQyqsEBCRxoNFLmhvzy9BkyepAEYJOTTnjct3JRUAdMKBxV8FMfUa3ao9U01TLy90Ww==",
      "encrypted_email_data": "D0P5UaervsZOlgFYt5SQbygrUvLoaV/jQsX1e2snmuR7uNcc0o9EuGeO36SCmChOaT6FOnSf0v5vP2o6QBxr5Ov6z1VlEpopZjHBnnsMVJkdb09hSdplmW39D5/txdY9mXlg0UYyIGnzy57wvDTjkgGG2r/vRTz+MqR+N6Ck3/767k6n43qNe8/AMoDLJ9wwVWxiohai9+qRf2Se5+BS18JxPuum98vzE4gYhuK/oMvOYGTYkLk7cr+TzRGEtgMfmbjKpJf5gCOZ8fUXAjQc",
      "encrypted_iv": "vVLFgDcY0hJi1ylDX2sO8A==",
      "public_key": "PUBLIC_KEY",
      "timestamp": 1734451731
   }

DELETE /v1/encrypted/email
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
      "success": true,
   }


Keys used in these examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Public Key**

.. code-block:: pem

   -----BEGIN PUBLIC KEY-----
   MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtZqCdquUjHek14rf7Wwl
   JTDwcVs9goxKwATXgcpKB+vL9qMeLnzztlKN+kKMUKh3oUuSKpR5le+JsawzCMyO
   tciHNa1eGr/Rj7QjR9tfmXu3WNNFQgKSVUCEnU238RLRW92Nn34YueYN1ANnm9LL
   Mly9BYIIrzGQca4+J6a3/nQ6OuP/ggTKfsLMR8F6WtFsfBbfo5eO1ZtS+bsh4CyX
   K//CDFuVBdLjCXqA9PPV5kTJAF2EoIE03dCi7JpqHwL2YtRYn/vDoS7/2VmHCHm1
   f4XZeQWco5xhmSXyguQzicxrD16O4QfNYuK34MhkrdGpRJLgUadht2m0hubE7g2M
   6wIDAQAB
   -----END PUBLIC KEY-----

**Private Key**

.. code-block:: pem

   -----BEGIN PRIVATE KEY-----
   MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC1moJ2q5SMd6TX
   it/tbCUlMPBxWz2CjErABNeBykoH68v2ox4ufPO2Uo36QoxQqHehS5IqlHmV74mx
   rDMIzI61yIc1rV4av9GPtCNH21+Ze7dY00VCApJVQISdTbfxEtFb3Y2ffhi55g3U
   A2eb0ssyXL0FggivMZBxrj4nprf+dDo64/+CBMp+wsxHwXpa0Wx8Ft+jl47Vm1L5
   uyHgLJcr/8IMW5UF0uMJeoD089XmRMkAXYSggTTd0KLsmmofAvZi1Fif+8OhLv/Z
   WYcIebV/hdl5BZyjnGGZJfKC5DOJzGsPXo7hB81i4rfgyGSt0alEkuBRp2G3abSG
   5sTuDYzrAgMBAAECggEAKLvbf5rE2y0LAH3Z9HtJaaoshICer2WgbqmnXSluqZAu
   U8gKwQqt77tctUGwD3d6PeehhYOAMi1kiUHCwLqBWCz+hv+4F+/mpYEWWMvQCbFC
   Ut4wrrm88PpjxJTmKWC7LQvo9FloWmpLt757wuvpQAalL1MXd5R6fcVDk8lFhAFU
   IKtQLmG3ZK7bV+X3epXpyeys1ujSQGq4O7dAb8iuXpWHx0CHNZcOOiuzdR9yOrV4
   1sdmsi0TGXZGLePsl1iaLQTcCUTyzz7BYKYvzyCxj+wE9MbtM2hojz+Rz/tqBIyR
   Ibim1akVFjzY9H88PbzbQGZkq+YgXV2OF6ezkWJZgQKBgQD7VXvfhpe4OsWukR2f
   4FxuOo+EFpzPUz4nVvraOVDLG5lcyJjhGSeFPEEnSx/r9+kB6/9IWVolNGC6hMkC
   fiaYOdDhljw5ww2Yd7m+SLVp7+9BJjT1yT4NkY3XZUSKfz5c1mzs6oWmvktmfZHN
   EZE0wbG2cqU3S1ElEiRtPlrz+wKBgQC4+Z4qinlwnOe640Tq+mXe15pTneC+ptlL
   AorZHk5HyvNqZ+if5S0lWxZsG+FMvavk9ZMDD0oT78UJ1uOK9Wg344KBltynrcJg
   ftG46dUkDZNOQt1vSx6o4aCWAOcG36tIjrvYd2FuwLMyKBGXCUAW76jcFz6yDxEL
   6s0nQPmH0QKBgBhRVBPzjNh5b0kNp2Uhqy/LILmyCmgQ8NGTm9/jbcrJF9SfYBNf
   gLBmfRNVNHh7WyMhd2jDpHI3GCjT0jMYi5ls9qXtCFS6Z6VZ6DHeDRd77JVMIhGp
   8AQWEjhGBxSzbRBEevONWXMhtF/tRF8oFPmayBwUCaJI+kfw8m9Tei9jAoGAfKRv
   aNkQhcqk97DnIrOB64w6yLds1utVJo9bAnzCYOwn4/6KqRvjtPVRAZ4zzeNNLiYw
   XvJxh0ec7Ulo4J0HEgnzSeFfZHnYre8m4MRoRDgFl8nErpbe3QvUit+mzWHwaB8O
   AwpGlDuzREvttmmcTxhFH7FmJNO0N+SLQzUsL9ECgYAKZJVf62Jxz1aXMaNCbjWu
   O3OdanHfNjOVPcLQoPmztUR1VzdZgrGXtLWXxLF8UTEG/VdkVulVzG8iqfJkhH1m
   ZqNY123aj6DYgkhBbe8N4IG9/Lm8NWStKph5lASsXHJYunmB4k8pxob9/DGlwJVQ
   dH2Y3rso/ZF0XpVccQlY4g==
   -----END PRIVATE KEY-----

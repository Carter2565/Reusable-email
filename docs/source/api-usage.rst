API Documentation
==================================

Base URL:
---------
http://api.reusable.email/v1

Endpoints
---------

Inbox Management
~~~~~~~~~~~~~~~~~

**Get Inbox**

- **URL:** `/inbox`
- **Method:** `GET`
- **Parameters:**
  - `alias` (string): The alias name of the inbox.
- **Description:** Fetches all emails in the specified inbox.

**Get Email**

- **URL:** `/email`
- **Method:** `GET`
- **Parameters:**
  - `alias` (string): The alias name of the inbox.
  - `id` (string): The email ID to fetch.
- **Description:** Fetches the details of a specific email in the inbox.

**Delete Email**

- **URL:** `/email`
- **Method:** `DELETE`
- **Parameters:**
  - `alias` (string): The alias name of the inbox.
  - `id` (string): The email ID to delete.
- **Description:** Deletes a specific email from the inbox.

Encrypted Inbox Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Note on Alias Format for Encrypted Operations**

Encrypted inbox aliases must follow this format: `^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$`

**Examples:**

- `A1B2-C3D4-E5F6`
- `ABCD-1234-EFGH`
- `1234-5678-9012`
- `1234-ABCD-5678`

**Create Encrypted Inbox**

- **URL:** `/encrypted/inbox`
- **Method:** `POST`
- **Data (JSON):**
  - `publicKey` (string): The public key encoded in UTF-8.
  - `inboxName` (string): The alias name in the required format.
- **Description:** Creates a new encrypted inbox.

**Get Encrypted Inbox**

- **URL:** `/encrypted/inbox`
- **Method:** `GET`
- **Parameters:**
  - `alias` (string): The alias name in the required format.
- **Description:** Fetches the details of an encrypted inbox.

**Get Encrypted Email**

- **URL:** `/encrypted/email`
- **Method:** `GET`
- **Parameters:**
  - `alias` (string): The alias name in the required format.
  - `id` (string): The email ID to fetch.
- **Description:** Fetches the details of a specific encrypted email.

**Delete Encrypted Email**

- **URL:** `/encrypted/email`
- **Method:** `DELETE`
- **Parameters:**
  - `alias` (string): The alias name in the required format.
  - `id` (string): The email ID to delete.
- **Description:** Deletes a specific encrypted email.

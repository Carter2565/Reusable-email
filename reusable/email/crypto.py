import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from .types import Email  


def generate_keys(public_exponent=65537, key_size=2048):
  """
  Generate a pair of RSA public and private keys.
  Args:
    public_exponent (int): Public exponent for the key generation.
    key_size (int): Size of the key in bits.

  Returns:
    tuple: Public key and private key in PEM format as bytes.
  """
  rsa_private_key = rsa.generate_private_key(
    public_exponent=public_exponent,
    key_size=key_size,
    backend=default_backend()
  )
  rsa_public_key = rsa_private_key.public_key()

  public_key = rsa_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
  )

  private_key = rsa_private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
  )

  return public_key, private_key


def decrypt_email(encrypted_email, rsa_private_key_pem):
  """
  Decrypt an email using RSA and AES encryption.
  Args:
    encrypted_email (dict): Dictionary containing encrypted AES key, IV, and email data (Base64 encoded).
    rsa_private_key_pem (str): RSA private key in PEM format as a string.

  Returns:
    Email: Decrypted email object, or None if decryption fails.
  """
  try:
    # Decode Base64-encoded encrypted parts
    encrypted_aes_key = base64.b64decode(encrypted_email['encrypted_aes_key'])
    encrypted_iv = base64.b64decode(encrypted_email['encrypted_iv'])
    encrypted_email_data = base64.b64decode(encrypted_email['encrypted_email_data'])

    # Load the RSA private key
    private_key = serialization.load_pem_private_key(
      rsa_private_key_pem.encode('utf-8'),
      password=None,
      backend=default_backend()
    )

    # Decrypt the AES key using RSA-OAEP
    aes_key = private_key.decrypt(
      encrypted_aes_key,
      padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
      )
    )

    # Decrypt the email content using AES-CFB
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(encrypted_iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_email_data = decryptor.update(encrypted_email_data) + decryptor.finalize()

    # Deserialize the decrypted email JSON to an Email object
    email = Email.from_json(decrypted_email_data.decode('utf-8'))
    return email

  except Exception as e:
    print(f"Error decrypting email: {e}")
    return None

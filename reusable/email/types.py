# type: ignore 
import json

class Email:
  def __init__(self, id: str, subject: str, sender: str, timestamp: float, body: str):
    self.id = id
    self.subject = subject
    self.sender = sender
    self.timestamp = timestamp
    self.body = body

  @classmethod
  def from_json(cls, decrypted_email_data: str):
    # Parse JSON and create an Email instance
    email_json = json.loads(decrypted_email_data)
    return cls(
      id=email_json.get('id', None),
      subject=email_json.get('subject', None),
      sender=email_json.get('sender', None),
      timestamp=email_json.get('timestamp', None),
      body=email_json.get('body', None)
    )
  
  @classmethod
  def to_json(cls, email_instance):
    # Convert Email instance to JSON string
    email_dict = {
      'id': email_instance.id,
      'subject': email_instance.subject,
      'sender': email_instance.sender,
      'timestamp': email_instance.timestamp,
      'body': email_instance.body
    }
    return json.dumps(email_dict)


Inbox = list[Email]
  
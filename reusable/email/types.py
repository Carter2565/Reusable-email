# type: ignore 

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
      id=email_json['id'],
      subject=email_json['subject'],
      sender=email_json['sender'],
      timestamp=email_json['timestamp'],
      body=email_json['body']
    )
  

Inbox = list[Email]
  
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your Twilio credentials (stored in .env)
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(account_sid, auth_token)

# Replace with actual phone number
to_number = "+1XXXXXXXXXX"

message = client.messages.create(
    to="+13156642151",
    from_=twilio_number,
    body="This is a test message from your SMS system!"
)

print("Message sent. SID:", message.sid)


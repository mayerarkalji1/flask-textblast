import pandas as pd
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load credentials
load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(account_sid, auth_token)

# Load contacts from CSV
contacts = pd.read_csv("contacts.csv")

# Message to send
template = "Hi {name}, this is a test message from your SMS system."

# Send message to each contact
for index, row in contacts.iterrows():
    name = row["name"]
    phone = row["phone"]
    message_text = template.format(name=name)

    try:
        message = client.messages.create(
            to=phone,
            from_=twilio_number,
            body=message_text
        )
        print(f"Sent to {name} ({phone}): SID {message.sid}")
    except Exception as e:
        print(f"Failed to send to {name} ({phone}): {e}")


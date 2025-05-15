import os
import time
import pandas as pd
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
client = Client(account_sid, auth_token)

TASKS_FILE = "scheduled/tasks.txt"

def send_group_message(group_name, msg_template):
    try:
        df = pd.read_csv(f"groups/{group_name}.csv", encoding='latin1')
        df.columns = [col.lower().strip() for col in df.columns]

        for _, row in df.iterrows():
            name = row.get("name", "")
            phone = (
                row.get("phone") or
                row.get("phone number") or
                row.get("mobile") or
                row.get("number")
            )
            message_text = msg_template.format(name=name)
            print(f"Sending to {name} ({phone})")

            message = client.messages.create(
                to=phone,
                from_=twilio_number,
                body=message_text
            )
            print(f"✔️ Sent to {name} – SID: {message.sid}")
    except Exception as e:
        print(f"❌ Error sending group '{group_name}': {e}")

def check_and_run_tasks():
    if not os.path.exists(TASKS_FILE):
        return

    updated_tasks = []
    now = datetime.now()

    with open(TASKS_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        try:
            group_name, send_at_str, message = line.strip().split("|", 2)
            send_time = datetime.strptime(send_at_str, "%Y-%m-%d %H:%M")
            if send_time <= now:
                print(f"⏰ Sending scheduled group: {group_name} (was set for {send_at_str})")
                send_group_message(group_name, message)
            else:
                updated_tasks.append(line)
        except Exception as e:
            print(f"❌ Invalid task line: {line.strip()} — {e}")

    with open(TASKS_FILE, "w") as f:
        f.writelines(updated_tasks)

if __name__ == "__main__":
    print("📅 Scheduler started. Checking every 60 seconds...")
    while True:
        check_and_run_tasks()
        time.sleep(60)



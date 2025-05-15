from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route('/sms-reply', methods=['POST'])
def sms_reply():
    print("✅ Received POST from Twilio at /sms-reply")
    print("🔹 Form data:", request.form)

    # Build a Twilio XML response
    resp = MessagingResponse()
    resp.message("Thanks for your message!")

    return str(resp), 200

if __name__ == '__main__':
    # Render requires binding to 0.0.0.0 and using the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


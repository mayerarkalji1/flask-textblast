kfrom flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route('/sms-reply', methods=['POST'])
def sms_reply():
    print("✅ Received POST from Twilio at /sms-reply")
    print("🔹 Form data:", request.form)

    # Create the Twilio response
    resp = MessagingResponse()
    resp.message("Thanks for your message!")

    # Log the TwiML response for verification
    print("🔸 Responding with TwiML:", str(resp))

    return str(resp), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


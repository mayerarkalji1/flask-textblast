from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms-reply', methods=['POST'])
def sms_reply():
    print("✅ Received POST from Twilio at /sms-reply")
    print("🔹 Form data:", request.form)

    # Twilio expects a proper TwiML response
    resp = MessagingResponse()
    resp.message("Thanks for your message!")

    return str(resp), 200  # Return TwiML XML with 200 OK

@app.route('/test', methods=['POST'])
def test_route():
    print("✅ Received POST at /test")
    return "<Response><Message>OK</Message></Response>", 200, {'Content-Type': 'text/xml'}

if __name__ == '__main__':
    app.run(debug=True)


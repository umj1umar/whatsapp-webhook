from flask import Flask, request

import os

app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "default_verify")
PORT = int(os.getenv("PORT", 5000))


@app.get("/webhook")
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verified")
        return challenge, 200
    else:
        return "Verification failed", 403


@app.post("/webhook")
def receive_message():
    data = request.json
    print("Incoming WhatsApp Data:", data)
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)

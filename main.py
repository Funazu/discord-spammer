import config
import requests
import time
import threading
import json
import random

def send_message_periodically(token, json_path):
    print("[debug] Function send_message_periodically started")

    with open(json_path, 'r') as f:
        data = json.load(f)

    channel_id = data["channel_id"]
    messages = data["messages"]
    last_message = None

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    def loop():
        nonlocal last_message
        while True:
            message = random.choice(messages)
            while message == last_message and len(messages) > 1:
                message = random.choice(messages)

            last_message = message
            payload = {"content": message}
            url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
            try:
                response = requests.post(url, headers=headers, json=payload)
                if response.status_code in [200, 204]:
                    print(f"[chat] Sent: {message}")
                else:
                    print(f"[chat] Failed: {response.status_code} - {response.text}")
            except Exception as e:
                print(f"[chat] Error: {e}")
            time.sleep(config.TIME_SLEEP)

    threading.Thread(target=loop, daemon=True).start()

send_message_periodically(config.DISCORD_TOKEN, "messages.json")

while True:
    time.sleep(1)

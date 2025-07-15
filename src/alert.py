import requests
import time

class AlertManager:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_alert(self, message, retries=3):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        for attempt in range(retries):
            try:
                response = requests.post(url, data={"chat_id": self.chat_id, "text": message}, timeout=15)
                if response.status_code == 200:
                    return True
                else:
                    print(f"\033[91m[!] Telegram API error: {response.status_code}, {response.text}\033[0m")
            except requests.exceptions.Timeout:
                print(f"\033[91m[!] Timeout, retrying... ({attempt+1}/{retries})\033[0m")
                time.sleep(2)
        return False

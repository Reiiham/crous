# Config
import requests
import os 
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
city_filter = os.getenv("CITY_NAME")

url = "https://trouverunlogement.lescrous.fr/api/fr/search/41"

# Make the POST request
def get_available_rooms():
    try: 
        response = requests.post(url, json={})

        if response.status_code != 200:
            print("Error: Failed to fetch data")
            return  #return only here if error

        data = response.json()
        items = data.get("results", {}).get("items", [])
        found = False

        for item in items:
            entity = item["residence"].get("entity", {})
            entity_name = entity.get("name")

            if entity_name.lower() != city_filter.lower():
                continue  # Skip cities you don't want

            label = item.get("label", "No label")
            address = item["residence"].get("address", "No address")
            res_label = item["residence"].get("label", "No residence name")
            link = f"https://trouverunlogement.lescrous.fr/tools/41/accommodations/{item['id']}"
        
            message = (
                f"*{res_label}*\n"
                f" City: {entity_name}\n"
                f" Label: {label}\n"
                f" Address: {address}\n"
                f"[View Listing]({link})"
            )
            send_telegram(message)
            found = True
        
        if not found:
            print(f" No rooms found in {city_filter}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# Send message to Telegram
def send_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(telegram_url, data=payload)
        if response.status_code != 200:
            print(f" Failed to send message: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

# Run
if __name__ == "__main__":
    get_available_rooms()

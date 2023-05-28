import requests

BOT_API_KEY = "5902646689:AAFTBbITdTUjrqXCZuwhGcR1o893ybFttSc"
MY_CHANNEL_NAME = "@test_api_geo"


def bot_notification(name, geom, desc):
    longitude = geom.x
    latitude = geom.y
    response = requests.get(
        f"https://api.telegram.org/bot{BOT_API_KEY}/sendMessage",
        {
            "chat_id": MY_CHANNEL_NAME,
            "text": f"New place has been created \n"
            f"===== {name} ===== \n"
            f"===== Description ===== \n"
            f"{desc}\n"
            f"===== Coordinates ===== \n"
            f"Longitude --> {longitude} \n"
            f"Longitude --> {latitude} \n"
        },
    )

    if response.status_code == 200:
        print(
            f"Borrowing creating successfully sended to channel"
            f"  --> {MY_CHANNEL_NAME}  <-- "
        )
    else:
        print(response.text)


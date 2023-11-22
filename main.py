import os
import requests
import time
from datetime import datetime
import pytz
import random

CHECK_SNOWAGER = True
SNOWAGER_ASLEEP = False

PHRASES = [
    "I am feeling very sleepy. I think it is time for my nap. Zzz...",
    "I hope I don't forget to use Pokemon Sleep this time. Zzz...",
    "Draco Dormiens Nunquam Titillandus. Zzz...",
    "I am just a little worm who needs a little sleeb. Zzz...",
    "I sure do love all of my prized possessions! Zzz...",
    "I shouldn't have drank so much at Adam's super-mansion. Zzz...",
    "They may take my life, but they'll never take my Neggitus Injection. Zzz...",
    "I heard that RATR is an Overwatch god. Wait, what's a RATR? Zzz...",
    "Did you know that *wiggle wiggle wiggle wiggle wiggle*? Zzz...",
    "On a scale of 1-10, I'm feeling an absolute 10 for blasting. Zzz...",
    "You've got to ask yourself one question: Do I feel lucky? Well, do ya, punk? Zzz...",
    "Toto, I've a feeling we're not in Neopia Central anymore... Zzz...",
    "Hasta la vista, baby. Zzz...",
    "I don't wanna work! I just wanna play Neopets all day... Zzz...",
    "My name is Snowie, commander of the Armies of the North, General of Terror Mountain,"
    " loyal servant to the true emperor, Dr. Sloth. Father to a murdered son, husband to a murdered wife."
    " And I will have my vengeance, in this life or the next. Zzz...",
    "I'll get you my pretty, and your little Kacheek too! Zzz...",
    "I'm the king of the world! Zzz...",
    "The first rule of the Ice Caves is: You do not talk about the Ice Caves. Zzz...",
    "Hello. My name is Snowie. You killed my father. Prepare to die. Zzz...",
    "I am serious. And don't call me Shirley. It's Snowie. Zzz...",
    "Neggs? Where we're going we don't need Neggs. Zzz..."

]


API_KEY = os.environ["API_KEY"]
MESSAGE_API_URL = f"https://api.telegram.org/bot{API_KEY}/sendMessage"
UPDATES_API_URL = f"https://api.telegram.org/bot{API_KEY}/getMe"
GROUP_CHAT_ID = os.environ["GROUP_CHAT_ID"]
DEV_USER_ID = os.environ["DEV_USER_ID"]


PST = pytz.timezone('America/Los_Angeles')
SNOWAGER_TIMES = ["06:00", "14:00", "22:00"]


while CHECK_SNOWAGER:
    CURRENT_TIME_UTC = datetime.now(pytz.utc)
    CURRENT_TIME_PST = CURRENT_TIME_UTC.astimezone(PST)
    FORMATTED_TIME = CURRENT_TIME_PST.strftime("%H:%M")
    if FORMATTED_TIME in SNOWAGER_TIMES:
        SNOWAGER_ASLEEP = True

    if SNOWAGER_ASLEEP:
        RANDOM_PHRASE = random.choice(PHRASES)
        PARAMETERS = {
            "chat_id": GROUP_CHAT_ID,
            "text": f"{RANDOM_PHRASE}"
                    "\n https://www.grundos.cafe/winter/snowager/"
        }
        response = requests.post(MESSAGE_API_URL, params=PARAMETERS)
        response_data = response.json()
        response.raise_for_status()
        print(f"I announced myself as sleeping at {FORMATTED_TIME} NST.")
        SNOWAGER_ASLEEP = False

    print(SNOWAGER_TIMES)
    print(FORMATTED_TIME)
    time.sleep(60)


import os
import requests
from dotenv import load_dotenv

TG_API = os.getenv("BOT_API_KEY")

whook = '3a6793c0cb3edf.lhr.life'

r = requests.get(f'https://api.telegram.org/bot{TG_API}/setWebhook?url=https://{whook}/')

print(r.json())
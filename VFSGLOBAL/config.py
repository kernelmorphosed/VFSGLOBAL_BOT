import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
RUCAPTCHA_KEY = os.getenv('RUCAPTCHA_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

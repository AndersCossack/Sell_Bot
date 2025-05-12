from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='data/config.env')
API_BOT = os.getenv("API_BOT")

bot = Bot(token=API_BOT)
dp = Dispatcher()
"""
    Getting some env variable
"""

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv("TOKEN")
if TELEGRAM_TOKEN is None:
    raise Exception("Please enter your bot token to .env file")



from dotenv import load_dotenv
from os import getenv

load_dotenv()

DISCORD_TOKEN = getenv("DISCORD_TOKEN")
TIME_SLEEP = int(getenv("TIME_SLEEP", 60)) 

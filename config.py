from os import getenv
from dotenv import load_dotenv


admins = {}
load_dotenv()


api_id = int(getenv("api_id"))
api_hash = getenv("api_hash")
token = getenv("token")
session = getenv("session")

creator_id = int(getenv("creator_id"))
creator_name = getenv("creator_name")
creator_username = getenv("creator_username")

database_url = getenv("database_url")
bot_alive_image = getenv("bot_alive_image")
sudoers_id = list(map(int, getenv("sudoers_id").split()))
cmd_handler = list(getenv("cmd_handler", "/ . $ !").split())

support_group = getenv("support_group")
support_channel = getenv("support_channel")

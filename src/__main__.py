import asyncio as aio
from dotenv import load_dotenv
from util import get_env


load_dotenv()

APP_ID = get_env("APP_ID")
CLIENT_KEY = get_env("CLIENT_KEY")
CLIENT_SECRET = get_env("CLIENT_SECRET")
WEBHOOK_ADDRESS = get_env("WEBHOOK_ADDRESS")

async def main():
    # run fetch loop, every idk how many seconds.
    # if there are any new videos, trigger events to broadcast news on all subscribing channels.
    ...


if __name__ == "__main__":
    aio.run(main())

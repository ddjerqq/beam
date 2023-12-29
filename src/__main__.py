import asyncio as aio
from dotenv import load_dotenv

from src.video_stream import VideoStream
from util import get_env


load_dotenv()

APP_ID = get_env("APP_ID")
CLIENT_KEY = get_env("CLIENT_KEY")
CLIENT_SECRET = get_env("CLIENT_SECRET")
WEBHOOK_ADDRESS = get_env("WEBHOOK_ADDRESS")
DELAY = int(get_env("DELAY", "60"))


async def loop():
    async for video in VideoStream(CLIENT_SECRET):
        print(video)


async def main():
    while True:
        try:
            await loop()
            await aio.sleep(DELAY)
        except Exception as e:
            print(f"Exception: {e}")


if __name__ == "__main__":
    aio.run(main())

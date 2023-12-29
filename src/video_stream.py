import httpx
from typing import AsyncIterator
from dataclasses import dataclass

from src.types.error import Error
from src.types.user_video_list_post_response_data import UserVideoListPostResponseData
from src.types.video import Video


API_URL = f"https://open.tiktokapis.com/v2/video/list/"


@dataclass
class Response:
    data: UserVideoListPostResponseData
    error: Error


class VideoStream:
    """
    A stream of videos from a user's TikTok account.
    """

    def __init__(self, user_id: str):
        self.user_id = user_id
        self._cursor = ...

    @property
    def _payload(self) -> dict[str, int]:
        return {
            "max_count": 10,
            "cursor": 0,
        }

    @property
    def _headers(self) -> dict[str, str]:
        return {

        }

    async def __aiter__(self) -> AsyncIterator[Video]:
        """
        Yields videos from the user's TikTok account.
        """


async def fetch() -> AsyncIterator[Video]:
    async with httpx.AsyncClient() as client:
        r = await client.get('https://www.example.com/')


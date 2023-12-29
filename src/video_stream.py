import httpx
from typing import AsyncIterator
from dataclasses import dataclass
from time import time

from src.types.error import Error
from src.types.user_video_list_post_response_data import UserVideoListPostResponseData
from src.types.video import Video


API_URL = f"https://open.tiktokapis.com/v2/video/list/"


@dataclass
class Response:
    data: UserVideoListPostResponseData
    error: Error

    def is_ok(self):
        return self.error.is_ok()


class VideoStream:
    """
    A stream of videos from a user's TikTok account.

    Example:

        async for video in VideoStream(token):
            process video
    """

    def __init__(self, token: str):
        self._token = token
        self._cursor = int(time())

    @property
    def _payload(self) -> dict[str, int]:
        return {
            "max_count": 10,
            "cursor": 0,
        }

    @property
    def _headers(self) -> dict[str, str]:
        return {
            "Accept": "application/json",
            "Authorization": f"Bearer {self._token}",
        }

    async def __aiter__(self) -> AsyncIterator[Video]:
        """
        Yields videos from the user's TikTok account.
        """
        async with httpx.AsyncClient() as client:
            while True:
                response = await client.post(
                    API_URL,
                    headers=self._headers,
                    json=self._payload,
                )

                if not response.is_success:
                    print(f"Received status code {response.status_code} from TikTok API.")
                    break

                payload = Response(**response.json())

                if not payload.is_ok():
                    print(f"Received error from TikTok API: {payload.error}")
                    break

                for video in payload.data.videos:
                    yield video

                if payload.data.has_more:
                    self._cursor = payload.data.cursor
                else:
                    break

        raise StopAsyncIteration

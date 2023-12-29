from dataclasses import dataclass

from src.types.video import Video


@dataclass
class UserVideoListPostResponseData:
    """Tiktok API response data for POST /v2/video/list/"""

    videos: list[Video]
    """A list of video objects"""

    cursor: int
    """
    Cursor for pagination. If response.has_more is true, pass in the 
    response.cursor to the next request will yield the results for the 
    next page.

    Note: the cursor value is a UTC Unix timestamp in milli-seconds. 
    You can pass in a customized timestamp to fetch the user's videos 
    posted before the provided timestamp.
    """

    has_more: bool
    """Whether there are more videos"""

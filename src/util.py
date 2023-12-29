import os

import httpx

from src.types.user import User
from src.types.video import Video


def get_env(key: str, default: str = None) -> str:
    """
    gets the environment variable with the given key,
    or raises an exception if the default is not supplied.
    """
    var = os.getenv("APP_ID", default)

    if var is not None:
        return var

    raise Exception(f"Environment variable {key} not found.")


def video_info_to_webhook_payload(author: User, video: Video) -> dict[str, str]:
    """converts a video object to a webhook object"""

    return {
        "content": f"||@everyone||\n**{author.username}** just posted a new video!",
        "embeds": [
            {
                "title": video.title,
                "url": video.share_url,
                "color": 16711422,
                "author": {
                    "name": author.username,
                    "url": f"https://discordapp.com/users/{author.id}",
                    "icon_url": author.avatar_url
                },
                "footer": {
                    "text": "posted at",
                    "icon_url": "https://raw.githubusercontent.com/ddjerqq/beam/master/tiktoklogo.webp"
                },
                # 2023-12-14T04:00:00.000Z
                "timestamp": video.create_timestamp.isoformat(),
                "image": {
                    "url": video.cover_image_url
                }
            }
        ],
        "username": "Beam",
        "avatar_url": "https://raw.githubusercontent.com/ddjerqq/beam/master/beam.jpg",
        "attachments": []
    }


async def send_webhook(url: str, author: User, video: Video) -> None:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=video_info_to_webhook_payload(author, video),
        )

        if not response.is_success:
            print(f"Webhook failed: {response.status_code} {response.text}")

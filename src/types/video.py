from dataclasses import dataclass


@dataclass
class Video:
    """Tiktok video object"""

    id: str
    """Unique identifier for the TikTok video. Also called "item_id"""

    create_time: int
    """UTC Unix epoch (in seconds) of when the TikTok video was posted."""

    cover_image_url: str
    """A CDN link for the video's cover image. The image is static. Due to our trust and safety policies, the link has a TTL of 6 hours."""

    share_url: str
    """A shareable link for this TikTok video. Note that the website behaves differently on Mobile and Desktop devices."""

    video_description: str
    """The description that the creator has set for the TikTok video. Max length: 150"""

    duration: int
    """The duration of the TikTok video in seconds."""

    height: int
    """The height of the TikTok video."""

    width: int
    """The width of the TikTok video."""

    title: str
    """The video title. Max length: 150"""

    embed_html: str
    """HTML code for embedded video"""

    embed_link: str
    """Video embed link of tiktok.com"""

    like_count: int
    """Number of likes for the video"""

    comment_count: int
    """Number of comments on the video"""

    share_count: int
    """Number of shares of the video"""

    view_count: int
    """Number of views of the video"""

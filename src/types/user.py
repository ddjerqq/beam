from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    avatar_url: str

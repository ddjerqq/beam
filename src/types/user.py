from dataclasses import dataclass


@dataclass
class User:
    id: str
    username: str
    avatar_url: str

from dataclasses import dataclass


@dataclass
class Error:
    """Tiktok error object"""

    code: str
    """The error category in string"""

    message: str
    """The detailed error description"""

    log_id: str
    """The unique id associated with every request for debugging purpose"""

    def is_ok(self):
        return self.code == "ok"

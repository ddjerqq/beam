import os


def get_env(key: str) -> str:
    """
    gets the environment variable with the given key, or raises an exception.
    """
    var = os.getenv("APP_ID")

    if var is None:
        raise Exception(f"Environment variable {key} not found.")

    return var

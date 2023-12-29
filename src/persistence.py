import sqlite3


class DbContext:
    def __init__(self, db_path: str) -> None:
        self._db_path = db_path
        self._connection = sqlite3.connect(self._db_path)
        self._cursor = self._connection.cursor()

    def close(self):
        self._connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

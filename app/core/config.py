import os

class Config:
    DATABASE_URL: str

    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL")

        if not self.DATABASE_URL:
            raise RuntimeError("DATABASE_URL is not set")

config = Config()
import os

db_path: str = os.getenv("DB_PATH")  # type: ignore
static_path: str = os.getenv("STATIC_PATH")  # type: ignore

assert db_path is not None
assert static_path is not None

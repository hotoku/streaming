import os

db_path: str = os.getenv("DB_PATH")  # type: ignore
resource_path: str = os.getenv("RESOURCE_PATH")  # type: ignore

assert db_path is not None
assert resource_path is not None

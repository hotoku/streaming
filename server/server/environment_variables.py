import os

db_path: str = os.getenv("DB_PATH")  # type: ignore
resource_path: str = os.getenv("RESOURCE_PATH")  # type: ignore
static_path: str = os.getenv("STATIC_PATH")
port: int = int(os.getenv("PORT") or 80)

assert db_path is not None
assert resource_path is not None

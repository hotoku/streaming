import os

db_path: str = os.getenv("DB_PATH")  # type: ignore
resource_path: str = os.getenv("RESOURCE_PATH")  # type: ignore
uploaded_path: str = os.getenv("UPLOADED_PATH")  # type: ignore
root_path: str = os.getenv("ROOT_PATH") or os.getcwd()

if not os.path.exists(uploaded_path):
    os.makedirs(uploaded_path, exist_ok=True)


port: int = int(os.getenv("PORT") or 8080)


assert db_path is not None
assert resource_path is not None
assert uploaded_path is not None

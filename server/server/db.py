import sqlite3
import os
from sqlite3.dbapi2 import Cursor
from typing import Any, Iterable, List, Mapping


def db_path() -> str:
    ret = os.getenv("DB_PATH")
    if ret is None:
        raise RuntimeError("DB_PATH env var is not set")
    return ret


def connect() -> sqlite3.Connection:
    ret = sqlite3.connect(db_path())
    ret.row_factory = sqlite3.Row
    return ret


def random_list(n: int = 100) -> Iterable[Mapping[str, Any]]:
    con = connect()
    cur = con.cursor()
    ret = cur.execute(f"""
    select
      id,
      video_path,
      thumbnail_path
    from
      videos
    order by
      random()
    limit {n}
    """)
    return ret

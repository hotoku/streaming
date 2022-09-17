import sqlite3
import os
from typing import List
from dataclasses import dataclass

from . import environment_variables as ev


@dataclass
class DbRecord:
    id: int
    video_path: str
    thumbnail_path: str


def db_path() -> str:
    ret = ev.db_path
    if ret is None:
        raise RuntimeError("DB_PATH env var is not set")
    return ret


def get_video(id: int) -> DbRecord:
    con = connect()
    cur = con.cursor()
    ret = cur.execute(f"""
    select
      id,
      video_path,
      thumbnail_path
    from
      videos
    where
      id = {id}
    """)
    obj = next(ret)
    return DbRecord(
        obj["id"],
        obj["video_path"],
        obj["thumbnail_path"]
    )


def connect() -> sqlite3.Connection:
    ret = sqlite3.connect(db_path())
    ret.row_factory = sqlite3.Row
    return ret


def random_list(n: int = 100) -> List[DbRecord]:
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
    return [
        DbRecord(
            r["id"],
            r["video_path"],
            r["thumbnail_path"]
        )
        for r in ret
    ]

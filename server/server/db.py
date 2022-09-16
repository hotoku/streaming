import sqlite3
import os


def db_path() -> str:
    ret = os.getenv("DB_PATH")
    if ret is None:
        raise RuntimeError("DB_PATH env var is not set")
    return ret


def connect() -> sqlite3.Connection:
    ret = sqlite3.connect(db_path())
    ret.row_factory = sqlite3.Row
    return ret


def random_list():
    con = connect()
    cur = con.cursor()
    ret = cur.execute("select * from videos")
    return [r for r in ret]

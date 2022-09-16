#!/usr/bin/env python

import logging
import json
from typing import Iterable, Mapping
import sqlite3

import click

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO
)


@click.command()
@click.argument("db-path", type=click.Path(exists=True, dir_okay=False))
@click.argument("json-path", type=click.Path(exists=True, dir_okay=False))
def main(db_path: str, json_path: str):
    LOGGER.info("json_path=%s", json_path)
    info: Iterable[Mapping[str, str]] = json.load(open(json_path))

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.executemany(
        "insert into videos (video_path, thumbnail_path) values (?, ?)",
        [(d["video"], d["thumbnail"]) for d in info]
    )
    con.commit()


if __name__ == "__main__":
    main()

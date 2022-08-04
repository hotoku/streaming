from glob import glob
import sqlite3
from pathlib import Path

import click


def to_names(files: list[str]) -> list[str]:
    paths = [Path(s) for s in files]
    return [p.name for p in paths]


def doit(cur: sqlite3.Cursor, root_dir: str) -> None:
    files = glob(f"{root_dir}/**")
    names = to_names(files)

    cur.executemany("""
    insert into videos (path, name) values (?, ?);
    """, zip(files, names))


@click.command()
@click.argument("db_file", type=click.Path(exists=True, dir_okay=False, writable=True))
def main(db_file: str) -> None:
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    doit(cur, "/Volumes/data2/misc1")

    con.commit()


if __name__ == "__main__":
    main()

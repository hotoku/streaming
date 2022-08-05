from glob import glob
import sqlite3
from pathlib import Path
import subprocess as sp
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass


import click


class ThumbnailConvertError(Exception):
    pass


def to_names(files: list[str]) -> list[str]:
    paths = [Path(s) for s in files]
    return [p.name for p in paths]


def make_thumbnail_1(src_path: str, resource_dir: str) -> str:
    dest_path = str(
        (Path(resource_dir) / Path(src_path).name).resolve()) + ".png"

    ret = sp.run(
        [
            "ffmpeg",
            "-i",
            src_path,
            "-ss",
            "00:01:00.000",
            "-y",
            "-vframes",
            "1",
            dest_path
        ],
        stdout=sp.PIPE,
        stderr=sp.PIPE,
        text=True
    )
    if ret.returncode != 0:
        raise ThumbnailConvertError(
            f"stdout={ret.stdout}, stderr={ret.stderr}")
    return dest_path


def make_thumbnail(src_files: list[str], resource_dir: str) -> list[str | None]:
    # make_thumbnail_1(src_files[0], resource_dir)
    with ProcessPoolExecutor(max_workers=None) as ex:
        fs = [
            ex.submit(make_thumbnail_1, f, resource_dir)
            for f in src_files
        ]
    return [
        f.result() if not f.exception() else None
        for f in fs
    ]


def doit(cur: sqlite3.Cursor, root_dir: str, resource_dir) -> None:
    files = glob(f"{root_dir}/**")[:100]
    thumbs = make_thumbnail(files, resource_dir)
    names = to_names(files)
    assert len(files) == len(thumbs) == len(names)

    cur.executemany("""
    insert into videos (source_path, name, thumbnail_path) values (?, ?, ?);
    """, zip(files, names, thumbs))


@click.command()
@click.argument("db_file", type=click.Path(exists=True, dir_okay=False, writable=True))
@click.argument("resource_dir", type=click.Path(exists=True, file_okay=False, writable=True))
def main(db_file: str, resource_dir: str) -> None:
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    doit(cur, "/Volumes/data2/misc1", resource_dir)

    con.commit()


if __name__ == "__main__":
    main()

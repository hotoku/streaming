from typing import Any, List, Optional, Union
import re
import pathlib as pl
import os
import json

import click
from click.core import Context, Parameter
from click.types import ParamType
import luigi

from .tasks import Thumbnail


class StrList(ParamType):
    name = "list of strings"

    def convert(self,
                value: Any,
                param: Optional[Parameter],
                ctx: Optional[Context]) -> Any:
        param, ctx
        if type(value) is list:
            return value
        if type(value) is str:
            return value.split(",")
        return []

    def __call__(self,
                 value: Any,
                 param: Optional[Parameter] = None,
                 ctx: Optional[Context] = None) -> Any:
        if value is None:
            return None
        return self.convert(value, param, ctx)


def make_relative(root: str, path: str) -> str:
    p1 = str(pl.Path(root).resolve())
    p2 = str(pl.Path(path).resolve())
    assert p2.startswith(p1)
    return os.path.join(root, re.sub(f"^{p1}/", "", p2))


def make_absolute(s: Union[str, pl.Path]) -> str:
    return str(pl.Path(s).resolve().absolute())


@click.command()
@click.argument("root-dir", type=click.Path(file_okay=False),
                help="The path to directory where our web app stores static resources.")
@click.argument("video-dirs", type=StrList(),
                help="The path to directory where our web app stores videos.")
@click.argument("dest-root", type=click.Path(file_okay=False),
                help="The path to directory where our web app stores thumbnails.")
@click.argument("json-path", type=click.Path(dir_okay=False))
@click.option("--extension", type=str, default="mp4")
def main(root_dir: str, video_dirs: List[str], dest_root: str, json_path: str,
         extension: str):
    root_dir = make_absolute(root_dir)
    video_dirs = list(map(make_absolute, video_dirs))
    dest_root = make_absolute(dest_root)

    if not os.path.exists(dest_root):
        os.makedirs(dest_root)

    files = [
        make_absolute(f) for d in video_dirs for f in pl.Path(d).glob(f"./**/*.{extension}")
    ]
    tasks = [
        Thumbnail(file, dest_root)
        for file in files
    ]
    luigi.build(
        tasks,
        local_scheduler=True,
        workers=4
    )
    info = [
        dict(
            video=make_relative(root_dir, f),
            thumbnail=make_relative(
                root_dir, Thumbnail.dest_path(f, dest_root))
        )
        for f in files
    ]
    json.dump(info, open(json_path, "w"))


if __name__ == "__main__":
    main()

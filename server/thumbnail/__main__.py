from typing import Any, Optional
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


@click.command()
@click.argument("root-dirs", type=StrList())
@click.argument("dest-root", type=click.Path(file_okay=False))
@click.option("--json-path", type=click.Path(dir_okay=False), default=".info.json")
@click.option("--extension", type=str, default="mp4")
def main(root_dirs: str, dest_root: str, json_path: str,
         extension: str):
    if not os.path.exists(dest_root):
        os.makedirs(dest_root)
    files = [
        str(f) for d in root_dirs for f in pl.Path(d).glob(f"./**/*.{extension}")
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
            video=f,
            thumbnail=make_relative(
                dest_root, Thumbnail.dest_path(f, dest_root))
        )
        for f in files
    ]
    json.dump(info, open(json_path, "w"))


if __name__ == "__main__":
    main()

from typing import Any, Dict, List, Optional, Union
import re
import pathlib as pl
import os
import json
from glob import glob

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


def make_relative(prefix_info: Dict[str, str], path: str) -> str:
    for k, v in prefix_info.items():
        print(k, v, path)
        rex = f"^{k}"
        if re.match(rex, path):
            return re.sub(f"^{k}", v, path)
    assert False


def make_absolute(s: Union[str, pl.Path]) -> str:
    return str(pl.Path(s).resolve().absolute())


@click.command()
@click.argument("prefix-info-path", type=click.Path(dir_okay=False))
@click.argument("video-dirs", type=StrList())
@click.argument("dest-root", type=click.Path(file_okay=False))
@click.argument("json-path", type=click.Path(dir_okay=False))
@click.option("--extension", type=str, default="mp4")
@click.option("--use-pathlib/--no-use-pathlib", default=False)
@click.option("--pos", type=str, default="00:00:00.010")
def main(prefix_info_path: str, video_dirs: List[str], dest_root: str, json_path: str,
         extension: str, use_pathlib: bool, pos: str):
    """Make thumbnails from videos in VIDEO-DIRS. Thumbnails are saved in DEST-ROOT. Resulting paths are reported in JSON-PATH.


    PREFIX-INFO-PATH is a path to a json file. The json should be an object. The object is considered as a mapping from keys to its values.
    Prefixes of reported paths are replaced using this mapping.

    VIDEO-DIRS is the paths of directories where our app stores videos.

    DEST-ROOT is the path of the directory where our app stores thumbnails.

    JSON-PATH is the path where paths of videos and thumbnails are reported.
    """

    video_dirs = list(map(make_absolute, video_dirs))
    dest_root = make_absolute(dest_root)

    if not os.path.exists(dest_root):
        os.makedirs(dest_root)

    if use_pathlib:
        files = [
            make_absolute(f) for d in video_dirs for f in pl.Path(d).glob(f"./**/*.{extension}")
        ]
    else:
        files = [
            make_absolute(f) for d in video_dirs for f in glob(f"{d}/**/*.{extension}")
        ]
    tasks = [
        Thumbnail(file, dest_root, pos)
        for file in files
    ]
    luigi.build(
        tasks,
        local_scheduler=True,
        workers=os.cpu_count()
    )
    prefix_info = json.load(open(prefix_info_path))
    info = [
        dict(
            video=make_relative(prefix_info, f),
            thumbnail=make_relative(
                prefix_info, Thumbnail.dest_path(f, dest_root))
        )
        for f in files
    ]
    json.dump(info, open(json_path, "w"))


if __name__ == "__main__":
    main()

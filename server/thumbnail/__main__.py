import pathlib as pl
import os

import click
import luigi

from .tasks import Thumbnail


@click.command()
@click.argument("root-dir", type=click.Path(exists=True, file_okay=False))
@click.argument("dest-root", type=click.Path(file_okay=False))
@click.option("--extension", type=str, default="mp4")
def main(root_dir: str, dest_root: str,
         extension: str):
    if not os.path.exists(dest_root):
        os.makedirs(dest_root)
    files = pl.Path(root_dir).glob(f"./**/*.{extension}")
    tasks = [
        Thumbnail(str(file), dest_root)
        for file in files
    ]
    luigi.build(
        tasks,
        local_scheduler=True,
        workers=4
    )


if __name__ == "__main__":
    main()

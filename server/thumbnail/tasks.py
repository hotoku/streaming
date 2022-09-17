import pathlib as pl
from hashlib import sha256
import subprocess as sp
import luigi


class ThumbnailConvertError(Exception):
    pass


def make_thumbnail(video: str, thumb: str, pos: str) -> None:
    ret = sp.run(
        [
            "ffmpeg",
            "-i",
            video,
            "-ss",
            pos,
            "-y",
            "-vframes",
            "1",
            thumb
        ],
        stdout=sp.PIPE,
        stderr=sp.PIPE,
        text=True
    )
    if ret.returncode != 0:
        raise ThumbnailConvertError(
            f"stdout={ret.stdout}, stderr={ret.stderr}")


class Thumbnail(luigi.Task):
    src_path: str = luigi.Parameter()  # type: ignore
    dest_root: str = luigi.Parameter(significant=False)  # type: ignore
    pos: str = luigi.Parameter(significant=False)  # type: ignore

    @staticmethod
    def dest_path(src_path: str, dest_root: str) -> str:
        ret = pl.Path(dest_root) / \
            (sha256(src_path.encode()).hexdigest() + ".jpg")
        return str(ret.resolve())

    def output(self) -> list[luigi.LocalTarget]:
        return [
            luigi.LocalTarget(self.dest_path(self.src_path,
                                             self.dest_root))
        ]

    def run(self):
        make_thumbnail(self.src_path,
                       self.dest_path(self.src_path,
                                      self.dest_root),
                       self.pos)

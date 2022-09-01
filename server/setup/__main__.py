#!/usr/bin/env python

import logging

import click

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
    level=logging.INFO
)


@click.command()
@click.argument("dirs", type=str)
@click.argument("outd", type=click.Path(file_okay=False))
def main(dirs: str, outd: str):
    LOGGER.info("dirs=%s", dirs)
    LOGGER.info("outd=%s", outd)
    dirs2 = dirs.split(",")


if __name__ == "__main__":
    main()

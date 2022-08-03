#!/usr/bin/env python

import logging
import click

LOGGER = logging.getLogger(__file__)


@click.command()
def main():
    print("main")

if __name__ == "__main__":
    main()

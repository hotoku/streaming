import logging
import click

from . import app as APP

LOGGER = logging.getLogger(__name__)


@click.command()
@click.option("-d", "--debug/--nodebu", type=bool, default=False)
def main(debug: bool):
    host = "127.0.0.1" if debug else "0.0.0.0"
    APP.run(host=host, port=8080, debug=debug)


if __name__ == "__main__":
    main()

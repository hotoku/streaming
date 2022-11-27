import logging
import click

from . import app as APP
from . import environment_variables as ev

LOGGER = logging.getLogger(__name__)


@click.command()
@click.option("-d", "--debug/--nodebu", type=bool, default=False)
def main(debug: bool):
    import os
    print(f"{os.getcwd()=}")
    host = "127.0.0.1" if debug else "0.0.0.0"
    APP.run(host=host, port=ev.port, debug=debug)


if __name__ == "__main__":
    main()

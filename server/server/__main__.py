import logging
import sqlite3
from typing import Any, Dict, List, Tuple
from pathlib import Path

import click
from flask import Flask, request

LOGGER: logging.Logger = logging.getLogger(__name__)
DB_PATH: Path = (Path(__file__).parent / ".." / "db" / "db.sqlite").resolve()

app: Flask = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def get_con() -> sqlite3.Connection:
    LOGGER.debug(DB_PATH)

    ret = sqlite3.connect(str(DB_PATH.resolve()))
    ret.row_factory = sqlite3.Row
    return ret


def setup_logger(debug: bool = False):
    logging.basicConfig(
        filename="server.log",
        level=logging.DEBUG if debug else logging.INFO
    )


@app.route("/videos", methods=["get"])
def videos() -> List[Tuple[int, str]]:
    con = get_con()
    cur = con.cursor()
    data = cur.execute("""
    select
      id,
      name
    from
      videos
    """)
    return [(row["id"], row["name"]) for row in data]


@app.route("/echo", methods=["post"])
def echo() -> Dict[str, Any]:
    data: Dict[str, Any] = request.get_json()  # type: ignore
    return data


@click.command()
@click.option("-d", "--debug/--nodebug", is_flag=True, default=False)
def main(debug: bool):
    setup_logger(debug)
    app.run(debug=True, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()

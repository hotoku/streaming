import logging
import sqlite3
from typing import Any
from pathlib import Path

import click
from flask import Flask, request, send_file
from flask.wrappers import Response

LOGGER: logging.Logger = logging.getLogger(__name__)
DB_PATH: Path = (Path(__file__).parent / ".." / "db" / "db.sqlite").resolve()
RESOURCE_PATH: Path = (Path(__file__).parent) / ".." / "resource"

app: Flask = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def get_con() -> sqlite3.Connection:
    ret = sqlite3.connect(str(DB_PATH.resolve()))
    ret.row_factory = sqlite3.Row
    return ret


def setup_logger(debug: bool = False):
    logging.basicConfig(
        filename="server.log",
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
    )


@app.route("/", methods=["get"])
def index():
    LOGGER.debug("index")
    return send_file(RESOURCE_PATH / "build" / "index.html",
                     mimetype="text/html")


@app.route("/static/js/main.4d55f991.js", methods=["get"])
def hoge():
    return send_file(RESOURCE_PATH / "build" / "static" / "main.4d55f991.js")


@app.route("/videos", methods=["get"])
def videos() -> list[dict[str, Any]]:
    con = get_con()
    cur = con.cursor()
    data = cur.execute("""
    select
      id,
      name
    from
      videos
    """)
    return [dict(id=row["id"], name=row["name"]) for row in data]


@app.route("/video/image/<int:id>", methods=["get"])
def video_image(id: int) -> Response:
    LOGGER.debug("id=%d", id)
    return send_file(RESOURCE_PATH / "man.jpg",
                     mimetype="image/jpg")  # type: ignore


@app.route("/video/<int:id>", methods=["get"])
def video_file(id: int) -> Response:
    LOGGER.debug("id=%s", id)
    return send_file(RESOURCE_PATH / "9.mp4",
                     mimetype="video/mp4")  # type: ignore


@app.route("/echo", methods=["post"])
def echo() -> dict[str, Any]:
    data: dict[str, Any] = request.get_json()  # type: ignore
    return data


@click.command()
@click.option("-d", "--debug/--nodebug", is_flag=True, default=False)
def main(debug: bool):
    setup_logger(debug)
    app.run(debug=True, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()

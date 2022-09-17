import os
from pathlib import Path
from flask import Flask, request, send_from_directory
from flask.helpers import send_file

from . import db
from . import environment_variables as ev

app: Flask = Flask("server")
app.json.ensure_ascii = False  # type: ignore


@app.route("/video/<path:path>")
def video(path: str):
    print("video =", path)
    return send_file(Path(ev.resource_path) / path,
                     mimetype="video/mp4")  # type: ignore


@app.route("/video/list")
def video_list():
    num = request.args.get("num") or "100"
    return db.random_list(int(num))


@app.route("/resource/<path:path>")
def resource(path: str):
    return send_from_directory(ev.resource_path, path)

import os
from pathlib import Path
from flask import Flask, request, send_from_directory
from flask.helpers import send_file

from . import db
from . import environment_variables as ev

app: Flask = Flask("server")
app.json.ensure_ascii = False  # type: ignore


@app.route("/video/<int:id>")
def video(id: int):
    path = request.args.get("path") or \
        db.get_video(id).video_path
    return send_file(Path(ev.resource_path) / path)


@app.route("/thumbnail/<int:id>")
def thumbnail(id: int):
    path = request.args.get("path") or \
        db.get_video(id).thumbnail_path
    return send_file(Path(ev.resource_path) / path)


@app.route("/video/list")
def video_list():
    num = request.args.get("num") or "100"
    return db.random_list(int(num))


@app.route("/resource/<path:path>")
def resource(path: str):
    return send_from_directory(ev.resource_path, path)

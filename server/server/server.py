import os
from flask import Flask, request, send_from_directory

from . import db
from . import environment_variables as ev

app: Flask = Flask("server", static_folder=ev.static_path)
app.json.ensure_ascii = False  # type: ignore


@app.route("/video/<int:id>")
def video(id: int):
    ret = db.get_video(id)


@app.route("/video/list")
def video_list():
    num = request.args.get("num") or "100"
    return db.random_list(int(num))


@app.route("/resource/<path:path>")
def resource(path: str):
    return send_from_directory(ev.static_path, path)

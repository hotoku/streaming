import base64
from pathlib import Path
import os

from flask import Flask, request, send_from_directory
from flask.helpers import send_file


from . import db
from . import environment_variables as ev


app: Flask = Flask("server",
                   static_folder=os.path.join(os.getcwd(),  "static"))
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
    num = request.args.get("num") or 100
    ret = db.random_list(int(num))
    return ret


@app.route("/resource/<path:path>")
def resource(path: str):
    return send_from_directory(ev.resource_path, path)


@app.post("/upload")
def upload():
    name = request.form["name"]
    content = request.form["content"]
    path = os.path.join(ev.uploaded_path, name)
    if os.path.exists(path):
        return "existing"
    with open(path, "wb") as f:
        val = base64.b64decode(content)
        f.write(val)
    return "ok"


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path: str):
    print(f"{path=}")
    return send_file(os.path.join(os.getcwd(), "index.html"))

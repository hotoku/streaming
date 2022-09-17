import os
from flask import Flask, request, send_from_directory

from . import db


app: Flask = Flask("server")
app.json.ensure_ascii = False  # type: ignore


@app.route("/video/list")
def video_list():
    num = request.args.get("num") or "100"
    return db.random_list(int(num))


@app.route("/static/hoge.json")
def resource():
    return send_from_directory("static", "hoge.json")

from flask import Flask, request

from . import db


app: Flask = Flask(__name__)
app.json.ensure_ascii = False  # type: ignore


@app.route("/video/list")
def video_list():
    num = request.args.get("num") or "100"
    return db.random_list(int(num))

from flask import Flask


app: Flask = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/video/list")
def video_list():
    return []

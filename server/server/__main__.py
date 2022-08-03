import logging
from typing import Any, Dict
import json

import click
from flask import Flask, request

LOGGER = logging.getLogger(__name__)
app = Flask(__name__)

@app.route("/echo", methods=["post"])
def echo() -> bytes:
    data: Dict[str, Any] = request.get_json() # type: ignore
    return json.dumps(data).encode("utf-8")

@click.command()
def main():
    app.run(debug=True, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()

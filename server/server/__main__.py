import logging
from typing import Any, Dict, List
import json

import click
from flask import Flask, request

LOGGER: logging.Logger = logging.getLogger(__name__)
app: Flask = Flask(__name__)

@app.route("/videos", methods=["get"])
def videos() -> List[str]:
    return ["a", "b"]

@app.route("/echo", methods=["post"])
def echo() -> Dict[str, Any]:    
    data: Dict[str, Any] = request.get_json() # type: ignore
    return data

@click.command()
def main():
    app.run(debug=True, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()

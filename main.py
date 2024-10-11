from flask import Flask
from flask import request
import json


app = Flask(__name__)


@app.get("/api/testGet")
def hello_world():
    data = request.args
    return data


@app.post("/api/testPost")
def testPost():
    data = request.data
    return json.loads(data)


if __name__ == "__main__":
    app.run()

import platform
import os
from flask import Flask

app = Flask(__name__)
h = platform.uname()[1]
username = os.environ["uname"]
@app.route('/')
def hello_world():
    return '<h1>Hello '+username+'</h1><br>Hostname :'+h

if __name__ == "__main__":
    app.run(host="0.0.0.0")

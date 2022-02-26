from flask import Flask, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/event_post", methods=["POST"])
def _x():
    content = request.json
    print(request)
    print(request.args)
    print(json.loads(request.get_data()))
    return "POSTED"

@app.route("/event_get", method=["GET"])
def _get():


app.run(host="0.0.0.0")
from flask import Flask, request, render_template
from flask_cors import CORS
import json

topics = ["dogs","cats","rubbish"]

topicdesc = ["this one is for dogs", 'this page is to report cute animals',"this is for garbage"]

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html",nposts = len(topics), topics = topics,topicdesc = topicdesc)

pins = ({"lon": 144.42, "lat": -37.7, "message" :"someones house is here"})
@app.route("/get_pins")
def _pins():
    return pins


@app.route("/event_post", methods=["POST"])
def _x():
    content = request.json
    print(request)
    print(request.args)
    print(json.loads(request.get_data()))
    return "POSTED"

app.run(host="0.0.0.0",debug= True)
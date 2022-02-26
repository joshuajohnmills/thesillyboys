from flask import Flask, request, render_template,jsonify
import json

topics = ["dogs","cats","rubbish"]

topicdesc = ["this one is for dogs", 'this page is to report cute animals',"this is for garbage"]

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",nposts = len(topics), topics = topics,topicdesc = topicdesc)

pins = {"posts":[{"lon": 144.98, "lat": -37.8199, "message" :"good food"},
                 {"lon": 144.91, "lat": -37.8236, "message" :"bad food"},
                 {"lon": 144.931, "lat": -37.8636, "message" :"good drinks"}]}

@app.route("/get_pins",methods = ["GET"])
def _pins():
    return pins


@app.route("/event_post", methods=["POST"])
def _x():
    added_pin = json.loads(request.get_data())
    pins["posts"].append(added_pin)
    print(pins)
    return "POSTED"

app.run(host="0.0.0.0",debug= True)
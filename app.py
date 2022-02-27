from flask import Flask, request, render_template,jsonify
import json
from mysql_connect import *

DBClient = Client()

topics = ["dogs","cats","rubbish"]

topicdesc = ["this one is for dogs", 'this page is to report cute animals',"this is for garbage"]

app = Flask(__name__)


@app.route("/")
def _index():
    return render_template("index.html")

@app.route("/map")
def _map():

    DBClient.__conn__()
    query_reponse  = DBClient.query(
        """
        SELECT crowd_name, crowd_desc
        FROM crowd
        limit 10;
        """
    )
    DBClient.close()
    crowds = [i["crowd_name"] for i in query_reponse]
    crowddesc = [i["crowd_desc"] for i in query_reponse]

    return render_template("map.html",nposts = len(crowds), topics = crowds,topicdesc = crowddesc)

@app.route("/get_pins/",methods = ["GET"])
def _pins():

    DBClient.__conn__()
    query_reponse  = DBClient.query(
        """
        SELECT rep_lat as lat, rep_lon as lon, rep_desc as message
        FROM report
        """
    )
    DBClient.close()

    pins = {"posts":query_reponse}
    
    return pins




@app.route("/event_post", methods=["POST"])
def _x():
    added_pin = json.loads(request.get_data())
    
    DBClient.__conn__()
    DBClient.insert(
        f"""
            INSERT INTO report (crowd_id,rep_lat,rep_lon,rep_desc, rep_time)
            VALUES (1,{added_pin["lat"]},{added_pin["lon"]},"{added_pin["message"]}", CURRENT_TIMESTAMP);
        """
    )
    DBClient.conn.commit()
    DBClient.close()

    return "POSTED"

app.run(host="0.0.0.0",debug= True)
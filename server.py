from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
DATA = []

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    DATA.append({
        "node": data.get("node"),
        "status": data.get("status"),
        "time": str(datetime.datetime.now())
    })
    return "ok"

@app.route("/data")
def data():
    return jsonify(DATA)

app.run(host="0.0.0.0", port=5000)

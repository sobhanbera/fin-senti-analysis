# create a flask app
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

# the default route of the API
@app.route("/")
def home():
    errorResponse = json.dumps({"message": "Permission denied!"})
    return jsonify(errorResponse)

# the route for the API to get the data
@app.route("/api", methods=["GET", "POST"])
def api():
    # get the data from the request
    text = str(request.form.get("videoid"))

    # predict the output data
    output = predict_class(text).lower()

    # return the output data
    response = json.dumps({"predictionCode": output})

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False, host="localhost", port=8000)

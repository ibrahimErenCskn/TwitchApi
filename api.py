from flask import Flask, jsonify, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    url = {
        "KatılımcıalarPost": "/katilimcilarPost",
        "KatılımcıalarGet": "/katilimcilarGet"
    }
    return jsonify(url)


@app.route("/katilimcilarPost", methods=['POST', 'GET'])
def katilimciPost():
    data = request.get_json()
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
    return ("İşlendi")

@app.route("/katilimcilarGet", methods=['GET'])
def katilimciGet():
    with open('data.json', 'r') as json_file:
        loaded_data = json.load(json_file)
    return jsonify(loaded_data)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from queryOntology import * 

app = Flask(__name__)
CORS(app)

@app.route("/translatedLabels", methods=['POST'])
def translatedLabels():
    result = getTranslatedLabels()
    return jsonify(result)

@app.route("/allAllergies")
def allergyList():
    result = getAllergy()
    return jsonify(result)

if __name__ == "__main__":
    app.run()

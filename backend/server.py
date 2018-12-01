from flask import Flask, request, jsonify
from flask_cors import CORS
from queryOntology import * 

app = Flask(__name__)
CORS(app)

@app.route("/translatedRo")
def translatedLabels():
    result = getTranslatedLabels(data)
    return result

@app.route("/allAllergies")
def allergyList():
    result = getAllergy(data)
    return result

if __name__ == "__main__":
    app.run()

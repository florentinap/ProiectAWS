from flask import Flask, request, jsonify
from flask_cors import CORS
from queryOntology import * 

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["POST"])
def translatedLabels():
    data = request.get_json()
    getTranslatedLabels(data)

    return "Done"


if __name__ == "__main__":
    app.run()

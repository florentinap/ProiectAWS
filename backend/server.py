#/* Copyright (C) Florentina Petcu - All Rights Reserved
# * Unauthorized copying of this file, via any medium is strictly prohibited
# * Proprietary and confidential
# * Written by Florentina Petcu <florentina.ptc@gmail.com>, December 2018
# */

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
    result = getAllAllergies()
    return jsonify(result)

@app.route("/allMedicines")
def medicineList():
    result = getAllMedicines()
    return jsonify(result)

@app.route("/allergyByMedicine", methods = ['POST', 'GET'])
def allergyByMedicine():
	medicine = = request.json['medicineName']
    result = getAllergyByMedicine()
    return jsonify(result)

@app.route("/medicineByAllergy", methods = ['POST', 'GET'])
def medicineByAllergy():
	medicine = = request.json['allergyName']
    result = getMedicineByAllergy()
    return jsonify(result)

if __name__ == "__main__":
    app.run()

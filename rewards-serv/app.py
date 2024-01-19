# app.py

from flask import Flask, jsonify
from use_cases.generate_random_number import generate_random_number

app = Flask(__name__)

@app.route('/rng', methods=['GET'])
def get_random_number():
    random_number = generate_random_number()
    return jsonify(random_number.to_dict())

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/rng', methods=['GET'])
def get_random_number():
    random_number = random.randint(1, 15)
    return jsonify({'rng': random_number})





from pets import pets
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pets')
def get_pets():
    return jsonify(pets)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
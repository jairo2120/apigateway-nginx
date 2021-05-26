from peoples import peoples
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/peoples')
def get_peoples():
    return jsonify(peoples)

if __name__ == '__main__':
    app.run(debug=True, port=4001)
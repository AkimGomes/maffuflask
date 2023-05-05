from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/frase')
def get_frase():
    return jsonify({'frase': 'Olá Mundo!'})


if __name__ == '__main__':
    app.run()

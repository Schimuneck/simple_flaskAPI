from flask import Flask, request
from flask import jsonify
app = Flask(__name__)


@app.route('/sensorterra/', methods=['POST'])
def newBook():
    data = request.json
    print('Received JSON: %s' % data)
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4996)


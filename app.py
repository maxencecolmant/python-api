from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    str = "value1", "value2", "value3", "value4", "value5", "value6"
    return jsonify(str)


@app.route('/hello2', methods=['GET'])
def hello2():
    return 'hello2'


app.run(debug=True, host='0.0.0.0', port=5000)

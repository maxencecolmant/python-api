from flask import Flask
from flask import jsonify
import psycopg2
import os 


app = Flask(__name__)

DATABASE_URL= os.environ.get("DATABASE_URL")

@app.route('/testdb', methods=['GET'])
def postgres_test():
    try:
      conn = psycopg2.connect(DATABASE_URL)
      conn.close()
      return "Database Connected"
    except:
      return "Error connexion Database"
    


@app.route('/film', methods=['GET'])
def hello2():
   str = "value1", "value2", "value3", "value4", "value5", "value6"
   return jsonify(str)


app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, Blueprint, url_for, jsonify
from flask_restplus import Resource, Api, apidoc
from flask_restplus_relative_swagger import FlaskRestplusRelativeSwagger
import psycopg2
import os

app = Flask(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/api')


class MyApi(Api):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = 'http' if '7070' in self.base_url else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)


api = MyApi(blueprint, doc='/doc/', version='1.0', title='My api',
            description="My api")


@api.documentation
def swagger_ui():
    return apidoc.ui_for(api)


app.register_blueprint(blueprint)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# Change Swagger relative path on server


DATABASE_URL = os.environ.get("DATABASE_URL")


@api.route('/testdb', methods=['GET'])
class postgres_test(Resource):
    def get(self):
        try:
            conn = psycopg2.connect(DATABASE_URL)
            conn.close()
            return "Database Connected"
        except:
            return "Error connexion Database"


@api.route('/film', methods=['GET'])
class hello2(Resource):
    def get(self):
        str = "value1", "value2", "value3", "value4", "value5", "value6"
        return jsonify(str)


api_doc = FlaskRestplusRelativeSwagger()
api_doc.init_app(app=app, url='/api/doc/')

app.run(debug=True, host='0.0.0.0', port=7070)

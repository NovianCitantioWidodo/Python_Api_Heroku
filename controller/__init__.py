from flask import Blueprint, Flask
from flask_restplus import Api

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='API Documentation',
          version='1.0',
          description='SERVICE API')   


from dto import api as dto_api_model
from controller.UserController import api as user
api.add_namespace(user, '/user')
api.add_namespace(dto_api_model)


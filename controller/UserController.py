from helper import response
from flask import request, jsonify
from flask_restplus import Namespace, Resource
from service.UserService import SignUp, Login, List, Detail, Delete, Edit
from helper.support import token_required, checkauth
from dto.UserValidator import signup_request, login_request, edit_request

secrets = 'super-secret'


api = Namespace('User API')

auth_header = {'x-header': {'name': 'x-header',
                           'in': 'header',
                           'type': 'string',
                           'description': 'Token JWT!'}}

@api.doc(params=auth_header)
@api.route('/list')
class ListUserController(Resource):
    @staticmethod
    def get():
        token = checkauth(request)
        if not token:
            return response.badRequest("error", 'Token is missing!')

        current_user = token_required(token)
        if not current_user:
            return response.badRequest("error", 'Token is invalid!')

        data = List()

        return response.success(message="sukses", values = data)

@api.doc(params=auth_header)
@api.route('/detail/<int:id>')
class DetailUserController(Resource):
    @staticmethod
    def get(id):
        token = checkauth(request)
        if not token:
            return response.badRequest("error", 'Token is missing!')

        current_user = token_required(token)
        if not current_user:
            return response.badRequest("error", 'Token is invalid!')

        data = Detail(id)

        return response.success(message="sukses", values = data)

@api.route('/signup')
@api.expect(signup_request)
class CreateUserController(Resource):
    @staticmethod
    def post():
        param = request.json
        data = SignUp(param)

        return data

@api.route('/login')
@api.expect(login_request)
class LoginUserController(Resource):
    @staticmethod
    def post():
        param = request.json
        data = Login(param)

        return data

@api.doc(params=auth_header)
@api.route('/edit/<int:id>')
@api.expect(edit_request)
class EditUserController(Resource):
    @api.expect()
    def put(self, id):
        token = checkauth(request)
        if not token:
            return response.badRequest("error", 'Token is missing!')

        current_user = token_required(token)
        if not current_user:
            return response.badRequest("error", 'Token is invalid!')

        param = request.json

        data = Edit(id, param)
        if data == True:
            return jsonify({'status':'ok', 'message':'updated data', 'id':id})
        else:
            return jsonify({'message':'data not found', 'id':id})

@api.doc(params=auth_header)
@api.route('/delete/<int:id>')
class DeleteUserController(Resource):
    @staticmethod
    def delete(id):
        token = checkauth(request)
        if not token:
            return response.badRequest("error", 'Token is missing!')

        current_user = token_required(token)
        if not current_user:
            return response.badRequest("error", 'Token is invalid!')

        data = Delete(id)
        if data == True:
            return jsonify({'status':'ok', 'message':'deleted data', 'id':id})
        else:
            return jsonify({'message':'data not found', 'id':id})
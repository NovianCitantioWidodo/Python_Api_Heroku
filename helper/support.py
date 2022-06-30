import jwt
from entity.model import User
from helper import response

secrets = 'super-secret'

def checkauth(request):
    try:
        if 'x-header' not in request.headers:    
            return None

        token = request.headers['x-header']
        return token

    except Exception as e:
        print(e)
        return None

def token_required(token):
    try:
        data = jwt.decode(token, secrets, algorithms="HS256")
        if not data['id']:
            return None

        current_user = User.query.filter_by(id=data['id']).first()
        if not current_user:
            return None

        return current_user

    except Exception as e:
        print(e)
        return None


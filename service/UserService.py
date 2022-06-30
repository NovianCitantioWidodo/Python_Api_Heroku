from flask import request, jsonify, make_response
import datetime
import bcrypt
import jwt
from entity.model import User
from entity import db
from helper import response

secrets = 'super-secret'

def SignUp(param):
    try:
        password = param['password'].encode("utf-8")
        pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        user = User(
            username = param["username"],
            full_name = param["fullname"],
            email = param["email"],
            password = pw_hash.decode("utf-8"),
            created_date=datetime.datetime.now().strftime("%Y-%m-%d %X")
            )
        
        email_validation = User.query.filter_by(email=param['email']).first()
        if email_validation:
            return jsonify({'msg': 'Email already exist!', 'code': '-1'})

        username_validation = User.query.filter_by(username=param['username']).first()
        if username_validation:
            return jsonify({'msg': 'Username already exist!', 'code': '-1'})

        # data = {
        #     "username": param["username"],
        #     "email": param["email"],
        #     "password": param["password"]
        # }

        # expires = datetime.timedelta(days=7)
        # expires_refresh = datetime.timedelta(days=7)

        # access_token = create_access_token(data, fresh=True, expires_delta=expires)
        # refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        db.session.add(user)
        db.session.commit()

        return response.success({
            "data": "ok",
        }, "Sukses menambahkan data")

    except Exception as e:
        return response.badRequest("error", print(e))

def Login(param):
    username = param['username']
    password = param['password'].encode("utf-8")

    user = User.query.filter_by(username=username).first()
    if not user:
        return make_response(jsonify({"msg": "Username not found!", "code": "-1"}),
                                401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    pw =  user.password
    if not pw:
        return make_response(jsonify({"msg": "Wrong Password!", "code": "-1"}), 404,
                                {'WWW-Authenticate': 'Basic realm="Login required!"'})

    hashed = pw.encode('utf-8')
    if bcrypt.checkpw(password, hashed):
        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)}, secrets)

    data = {}
    data = {
        "email":    user.email,
        "username": user.username,
        'time':     datetime.datetime.now(),
        "token":    token.decode("utf-8")
    }
    return response.success(values = data, message = "sukses")

def List():
    user_req = db.session.query(User).all()

    data = []
    for user in user_req:
        data.append({
            'id': user.id,
            'full_name': user.full_name,
            'username': user.username,
            'email': user.email
            })

    return data

def Detail(id):
    user = db.session.query(User).filter_by(id=id).first()
    if not user:
        return None

    data = {
            'id': user.id,
            'full_name': user.full_name,
            'username': user.username,
            'email': user.email
            }

    return data

def Delete(id):
    user = db.session.query(User).filter_by(id=id).first()
    if not user:
        return False

    db.session.delete(user)
    db.session.commit()

    return True

def Edit(id, param):
    user = db.session.query(User).filter_by(id=id).first()
    if not user:
        return False

    user.full_name= param['full_name']
    user.username=  param['username']
    user.email=     param['email']
    
    db.session.commit()
    return True
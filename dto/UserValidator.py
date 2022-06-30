from . import api
from flask_restplus import fields

class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'



signup_request = api.model('signup_request', {
    'username': fields.String(required=True, description='Username'),
    'full_name': fields.String(required=True, description='Full Name'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Password')
})

login_request = api.model('login_request', {
    'username': fields.String(required=True, description='username', example='admin'),
    'password': fields.String(required=True, description='password', example='admin')
})

edit_request = api.model('edit_request', {
    'username': fields.String(required=True, description='Username'),
    'full_name': fields.String(required=True, description='Full Name'),
    'email': fields.String(required=True, description='Email')
})

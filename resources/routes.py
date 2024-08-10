from flask_restful import Resource, Api
#
from global_utilities import app
#
from resources.user.login import Login
from resources.user.refresh_token import RefreshAccessToken
from resources.user.register import Register

api = Api(app)

api.add_resource(
    Register,
    '/register'
)

api.add_resource(
    RefreshAccessToken,
    '/refresh'
)
api.add_resource(
    Login,
    '/login'
)
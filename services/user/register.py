import traceback
#
from flask_jwt_extended import create_access_token, create_refresh_token
#
from abstractions.base_service import BaseService
from abstractions.exceptions import Exceptions
#
from database.nosql.user import UserRepository


class RegisterService(BaseService):
    def __init__(self):
        super().__init__()

    def do(self, data):

        self.logger.info("Attempting to insert the user data in database")
        try:

            user_id = UserRepository().insert(email_id=data.get("email"), password=data.get("password"), username=data.get("username") if data.get("username") else None)
            access_token = create_access_token(identity=user_id)
            refresh_token = create_refresh_token(identity=user_id)
        except Exceptions as err:
            raise err

        return access_token, refresh_token
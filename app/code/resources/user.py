from flask_restful import Resource
from models.user import UserModel

class UserList(Resource):
    def get(self):
        return {"users": list(map(lambda x: x.json(), UserModel.query.all()))}

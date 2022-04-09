from backend.model.users import UsersDAO
from flask import Flask, jsonify

class UsersController:
    def build_users_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['username'] = row[1]
        result['email'] = row[2]
        result['first_name'] = row[3]
        result['last_name'] = row[4]
        result['role_id'] = row[5]
        return result

    def getAllUsers(self):
        dao = UsersDAO()
        user_list = dao.getAllUsers()
        if not user_list:
            return jsonify("NO USERS FOUND"), 404
        else:
            result = []
            for row in user_list:
                result.append(self.build_users_dict(row))
            return jsonify(result)

    def getUsersById(self, u_id):
        dao = UsersDAO()
        row = dao.getUserById(u_id)
        if not row:
            return jsonify(Error="NOT FOUND"), 404
        else:
            users = self.build_users_dict(row)
            return jsonify(users)


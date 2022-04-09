from backend.model.assigned import AssignedDAO
from flask import Flask, jsonify

class AssignedController:

    def build_assigned_dict(self, row):
        result = {}
        result['time_id'] = row[0]
        result['time_date'] = str(row[1])
        result['start_time'] = str(row[2])
        result['end_time'] = str(row[3])
        result['u_id'] = row[4]
        result['first_name'] = row[5]
        result['last_name'] = row[6]
        return result

    def getAllAssigned(self):
        dao = AssignedDAO()
        assigned = dao.getAllAssigned()
        result = []
        for row in assigned:
            temp = self.build_assigned_dict(row)
            result.append(temp)
        return jsonify(result)

    def getAssignedByUser(self, u_id):
        dao = AssignedDAO()
        row = dao.getAssignedByUser(u_id)
        if not row:
            return jsonify(Error="NOT FOUND"), 404
        else:
            users = self.build_assigned_dict(row)
            return jsonify(users)

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from backend.controller.users import UsersController
from backend.controller.timeslot import TimeslotController
from backend.controller.assigned import AssignedController

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Hello"

@app.route("/users", methods = ['GET', 'POST'])
def getAllUsers():
    if request.method == 'GET':
        return UsersController().getAllUsers()
    # elif request.method == 'POST':
    #     return UsersController().addUser()
    # else:
    #     return jsonify("METHOD NOT ALLOWED"), 405

@app.route('/users/id=<int:u_id>', methods = ['GET', 'PUT', 'DELETE'])
def getUsersById(u_id):
    if request.method == 'GET':
        return UsersController().getUsersById(u_id)
    # elif request.method == 'PUT':
    #     return UsersController().updateUser(u_id, request.json)
    # elif request.method == 'DELETE':
    #     return UsersController().removeUser(u_id)
    # else:
    #     return jsonify("Method not allowed"), 405

@app.route("/timeslots", methods = ['GET', 'POST'])
def getAllTimeslots():
    if request.method == 'GET':
        return TimeslotController().getAllTimeslots()
    # elif request.method == 'POST':
    #     return TimeslotController().addTimeslot()
    # else:
    #     return jsonify("METHOD NOT ALLOWED"), 405

@app.route('/timeslots/id=<int:time_id>', methods = ['GET', 'PUT', 'DELETE'])
def getTimeslotById(time_id):
    if request.method == 'GET':
        return TimeslotController().getTimeslotById(time_id)
    # elif request.method == 'PUT':
    #     return TimeslotController().updateTimeslot(time_id, request.json)
    # elif request.method == 'DELETE':
    #     return TimeslotController().removeTimeslot(time_id)
    # else:
    #     return jsonify("Method not allowed"), 405

@app.route('/assigned', methods = ['GET', 'POST'])
def getAllAssigned():
    if request.method == 'GET':
        return AssignedController().getAllAssigned()
    elif request.method == 'POST':
        return AssignedController().AssignTimeslot()
    else:
        return jsonify("METHOD NOT ALLOWED"), 405

@app.route('/assigned/userid=<int:u_id>', methods = ['GET', 'PUT', 'DELETE'])
def getAssignedByUser(u_id):
    if request.method == 'GET':
        return AssignedController().getAssignedByUser(u_id)
    # elif request.method == 'PUT':
    #     return AssignedController().updateAssigned(time_id, request.json)
    # elif request.method == 'DELETE':
    #     return AssignedController().removeAssigned(time_id)
    # else:
    #     return jsonify("Method not allowed"), 405
if __name__ == '__main__':
    app.run(debug=True)
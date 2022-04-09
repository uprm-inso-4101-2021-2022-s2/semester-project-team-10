from backend.model.timeslot import TimeslotDAO
from flask import Flask, jsonify

class TimeslotController:

    def build_timeslot_dict(self, row):
        result = {}
        result['time_id'] = row[0]
        result['time_date'] = str(row[1])
        result['start_time'] = str(row[2])
        result['end_time'] = str(row[3])
        result['status'] = row[4]
        result['capacity'] = row[5]
        return result

    def getAllTimeslots(self):
        dao = TimeslotDAO()
        timeslots = dao.getAllTimeslots()
        result = []
        print(timeslots)
        for row in timeslots:
            temp = self.build_timeslot_dict(row)
            result.append(temp)
        return jsonify(result)

    def getTimeslotById(self, time_id):
        dao = TimeslotDAO()
        row = dao.getTimeSlotById(time_id)
        if not row:
            return jsonify(Error="NOT FOUND"), 404
        else:
            users = self.build_timeslot_dict(row)
            return jsonify(users)

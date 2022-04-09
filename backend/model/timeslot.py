from backend.config.dbconfig import pg_config
import psycopg2

class TimeslotDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='%s'" % (pg_config['dbname'], pg_config['user'],
                                                                              pg_config['password'],
                                                                              pg_config['dbport'], pg_config['dbhost'])

        self.conn = psycopg2.connect(connection_url)


    def getAllTimeslots(self):
        cursor = self.conn.cursor()
        query = """SELECT time_id, time_date, start_time, end_time, status, capacity
                    FROM timeslot 
                    ORDER BY time_id;"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTimeSlotById(self, time_id):
        cursor = self.conn.cursor()
        query = """SELECT time_id, time_date, start_time, end_time, status, capacity
                            FROM timeslot 
                            WHERE time_id = %s;"""
        cursor.execute(query, (time_id,))
        result = cursor.fetchone()
        return result
from backend.config.dbconfig import pg_config
import psycopg2

class AssignedDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='%s'" % (pg_config['dbname'], pg_config['user'],
                                                                              pg_config['password'],
                                                                              pg_config['dbport'], pg_config['dbhost'])

        self.conn = psycopg2.connect(connection_url)


    def getAllAssigned(self):
        cursor = self.conn.cursor()
        query = """SELECT time_id, time_date, start_time, end_time, u_id, first_name, last_name
                    FROM assigned natural inner join timeslot natural inner join users
                    ORDER BY u_id;"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAssignedByUser(self, u_id):
        cursor = self.conn.cursor()
        query = """SELECT time_id, time_date, start_time, end_time, u_id, first_name, last_name
                            FROM assigned natural inner join timeslot natural inner join users
                            WHERE u_id = %s;"""
        cursor.execute(query, (u_id,))
        result = cursor.fetchone()
        return result
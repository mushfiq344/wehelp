import MySQLdb

class Dbconnect():
    conn=" "
    c=" "
    def __init__(self):
        self.conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "",
                           db = "wehelp")
        self.c = self.conn.cursor()


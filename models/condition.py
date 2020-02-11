from dbconnect import Dbconnect

class Condition(Dbconnect):

    def validateInputRequest(self,text):
        if len(text)>0:
            return 1
        else:
            return 0
    # inserting into condition table

    def insertCondition(self,condition):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO conditions	(condition_text) VALUES (%s)", [condition])
        self.conn.commit()
        cur.close()


    def getCondition(self):

        cur = self.conn.cursor()
        cur.execute("SELECT * from conditions where id=(select max(id) from conditions)", ())
        self.conn.commit()
        myresult = cur.fetchall()
        cur.close()
        return myresult

# c=cur;conn=mysql.connection


from dbconnect import Dbconnect

class User(Dbconnect):
    def validatePutRequest(self,data):
        if 'id' in data:
            return 1
        else:
            return 0
    # inserting into condition table

    def updateUser(self,user):
        cur = self.conn.cursor()
        start="UPDATE users SET "
        end = " WHERE id=%s"
        params=[]
        totalParams=0

        if 'name' in user:
            start=start+"name=%s,"
            params.append(user['name'])
            totalParams=totalParams+1
        if 'email' in user:
            start=start+"email=%s,"
            params.append(user['email'])
            totalParams=totalParams+1

        start=start[:-1]
        sql=start+end


        if totalParams>0:
            params.append(user['id'])
            cur = self.conn.cursor()
            cur.execute(sql, params)
            self.conn.commit()
            cur.close()
            return "Update Completed"
        else:
            return "Not Enough Parameters To Update"


# c=cur;conn=mysql.connection
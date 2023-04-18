import cx_Oracle


class db_class:

    def __init__(self):
        self.getDBconn_Cursor()

    def getDBconn_Cursor(self):
        dsn=cx_Oracle.makedsn("localhost",1521,"xe")
        self.conn=cx_Oracle.connect("gwangju_a","dbdb",dsn)
        self.cursor=self.conn.cursor()
        #return conn, cursor

    def colname(self):
        return list(map(lambda x:x[0].lower(),self.cursor.description))
    def getfetchone(self,sql):

        self.cursor.execute(sql)
        col=self.colname()
        row=self.cursor.fetchone()
        if not row:
            return 
        self.db_close()

        return dict(zip(col,row))
    
    def getfetchall(self,sql):

        self.cursor.execute(sql)
        rows=self.cursor.fetchall()
        
        col=self.colname()
        all_list=list(map(lambda x: dict(zip(col,x,)),rows))
        self.db_close()
        return all_list
    
    def setCUD(self,sql):

        self.cursor.execute(sql)
        self.conn.commit()
        self.db_close()

    def db_close(self):
        
        self.cursor.close()
        self.conn.close()
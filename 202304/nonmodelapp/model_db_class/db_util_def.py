import cx_Oracle
#### 클래스 내부 모든 함수에는 매개변수 ㄴ딜 키워드를 넣어야합니다 
    # self 외부에서 접근가능 
    # 내부호출 

class DB_Util:
    
    # db  접속 함수 

    def __init__(self) :
        # 클래스 생성과 동시에 db 연결 및 커서 받아오는 기능 
        self.getDBconn_Cursor()


    def getDBconn_Cursor(self):
        dsn=cx_Oracle.makedsn("localhost",1521,"xe")
        self.conn=cx_Oracle.connect("gwangju_a","dbdb",dsn)
        self.cursor=self.conn.cursor()
        #return conn, cursor

    #  조회결과에서 컬럼명추출하기 기능정의
    def getColName(self):
        return list(map(lambda x: x[0].lower(),self.cursor.description))


    # 한건 조호하는 함수
    def getFetchOne(self,sql):
        try:
            self.cursor.execute(sql)

            row=self.cursor.fetchone()
            col=self.getColName()
            if not row:
                self.DBClose()
                return {"RS":"nodate"}
            dict_row=dict(zip(col,row))

            self.DBClose()
            return dict_row
        except Exception as e:
            self.DBClose()
            return {"rs": e}

    # 여러건 조회하는 함수
    def getFetchAll(self,sql):
        try:

            self.cursor.execute(sql)

            rows=self.cursor.fetchall()
            if not rows:
                self.DBClose()
                return {"rs": "nodate"}
            col=self.getColName()

            dict_rows=list(map(lambda x:dict(zip(col,x)),rows))
            self.DBClose()
            return dict_rows
        
        except Exception as e:
            self.DBClose()
            return {"rs": e}
    ### 데이터 입력 수정 삭제 기능 cud
    def setCUD(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()
        self.DBClose()


    # close
    def DBClose(self):
        self.cursor.close()
        self.conn.close()
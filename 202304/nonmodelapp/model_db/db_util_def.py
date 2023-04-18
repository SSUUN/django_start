import cx_Oracle


# db  접속 함수 
def getDBconn_Cursor():
    dsn=cx_Oracle.makedsn("localhost",1521,"xe")
    conn=cx_Oracle.connect("gwangju_a","dbdb",dsn)
    cursor=conn.cursor()
    return conn, cursor

#  조회결과에서 컬럼명추출하기 기능정의
def getColName(cursor):
    return list(map(lambda x: x[0].lower(),cursor.description))

# 한건 조호하는 함수
def getFetchOne(cursor,row):
    
    col=getColName(cursor)
    #row=cursor.fetchone()
    dict_row=dict(zip(col,row))
    
    return dict_row

# 여러건 조회하는 함수
def getFetchAll(cursor,rows):
    #rows=cursor.fetchall()
    col=getColName(cursor)
    dict_rows=list(map(lambda x:dict(zip(col,x)),rows))
    
    return dict_rows

# close
def DBClose(cursor,conn):
    cursor.close()
    conn.close()
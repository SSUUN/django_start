from nonmodelapp.model_db.db_util_def import  *



def getList(sql):
    conn,cursor=getDBconn_Cursor()

    
    cursor.execute(sql)
    rows=cursor.fetchall()
    mem_list=getFetchAll(cursor,rows)

    DBClose(cursor,conn)

    return mem_list

def getView(sql):
    conn,cursor=getDBconn_Cursor()
    
    cursor.execute(sql)
    rows=cursor.fetchone()
    mem_list=getFetchOne(cursor,rows)

    DBClose(cursor,conn)
    return mem_list

def setUpdate(sql):
    conn,cursor=getDBconn_Cursor()
    cursor.execute(sql)

    conn.commit()
    #mem_list=getFetchAll(cursor)
    DBClose(cursor,conn)
    #return mem_list




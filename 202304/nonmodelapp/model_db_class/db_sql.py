from nonmodelapp.model_db_class.db_util_def import  DB_Util



def getList(sql):
    db_util=DB_Util()
    ### 클래스 생성시키기 
    # 클래스 생성과 동시에 conncursor정보 가지고 있음
    # 클랫 내에 변수들은 별도로 박아옺 ㅏ얺아도 되면 ㅣㅈㄱ접 접근가능
   # db_util.cursor.execute(sql)
    #rows=db_util.cursor.fetchall()
    mem_list=db_util.getFetchAll(sql)

    #db_util.DBClose()

    return mem_list

def getView(sql):

    db_util=DB_Util()
    
    mem_list=db_util.getFetchOne(sql)

    return mem_list

def setCUD(sql):

    db_util=DB_Util()
    db_util.setCUD(sql)

    return True

### 회원 한건 조회하기 f
#from nonmodelapp.model_db.db_util_def import  *
### 회원 한건 조회하기 f
from nonmodelapp.model_db_class import  db_sql



def getMemberList1():
    sql=f"""
        select mem_id,mem_pass,mem_name,mem_add1
        from member
        """
    return db_sql.getList(sql)

def getMember(mem_id):
    
    sql=f"""
        select mem_id,mem_pass,mem_name,mem_add1
        from member
        where mem_id='{mem_id}'
        """
    return db_sql.getView(sql)

def getMemberUpdate(mem_id,mem_pass,mem_add1):

    sql=f"""
        update member
            set mem_pass='{mem_pass}',
                mem_add1='{mem_add1}'

            where mem_id='{mem_id}'
        """
    return db_sql.setUpdate(sql)

def getloginChk(mem_id,mem_pass):

    sql=f"""
        select mem_id,mem_pass,mem_name,mem_add1
        from member
        where mem_id='{mem_id}'
            and mem_pass='{mem_pass}'
        """
    return db_sql.getView(sql)
from thirdapp.model_db_class.db_model_class import db_class



def getlist(sql):
    db=db_class()

    all_list=db.getfetchall(sql)
    
    return all_list

def getview(sql):

    db=db_class()
    view=db.getfetchone(sql)
    return view

def setCUD(sql):

    db=db_class()
    db.setCUD(sql)

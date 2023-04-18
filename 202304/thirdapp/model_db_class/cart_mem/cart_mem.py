from thirdapp.model_db_class.db_sql import *



def cart_mem_list(col,desc):

    sql="""
        select mem_id,mem_name,mem_add1,cart_no,cart_prod,cart_qty
        from member m inner join cart c
            on(m.mem_id=c.cart_member)
    """
    if col:
        sql+=f" order by {col}"
    if desc=="1":
        sql+=" desc"
    print(sql)
    return getlist(sql)

def cart_mem_view(cart_no,cart_prod):

    sql=f"""
        select mem_id,mem_name,mem_add1,cart_no,cart_prod,cart_qty
        from member m inner join cart c
            on(m.mem_id=c.cart_member)
        where cart_no='{cart_no}'
        and cart_prod='{cart_prod}'
        
        
    """
    return getview(sql)

def cart_mem_update(cart_no,cart_prod,cart_qty):

    sql=f"""
        update cart
            set cart_qty={cart_qty}
            where cart_no='{cart_no}'
                and cart_prod='{cart_prod}'
       
        
        
    """
    return setCUD(sql)


def cart_mem_delete(cart_no,cart_prod):

    sql=f"""
        delete from cart
            where cart_no='{cart_no}'
            and cart_prod='{cart_prod}'
       
        
        
    """
    return setCUD(sql)

def cart_mem_insert_form(mem_id):

    sql=f"""
        select mem_id,mem_name,mem_add1
        from member
        where mem_id='{mem_id}'
    """
    sql2=f"""
        select distinct(cart_prod),PROD_NAME 
        from cart c inner join  prod p
        on (c.cart_prod=p.PROD_ID)


    """

    return getview(sql),getlist(sql2)


def cart_mem_insert(mem_id,cart_prod,cart_qty):


    sql1="""select to_char(sysdate,'YYYYMMDD')|| lpad(nvl((select to_char(max(to_number(substr(cart_no,9)))+1) as cart_no
                            from cart
                            where substr(cart_no,0,8)=to_char(sysdate,'YYYYMMDD')),'1'),5,'0')
                    from dual"""
    
    sql=f"""
        insert into cart (cart_member,cart_prod,cart_no,cart_qty)
        values('{mem_id}','{cart_prod}',
                ({sql1})
    ,{cart_qty})
    """
    
    print(sql)
    cart_no=getview(sql1)
    setCUD(sql)
    return list(cart_no.values())[0]


def login_fprm(mem_id,mem_pass):
    sql=f"""
        select mem_id,mem_pass,mem_name
        from member
        where mem_id='{mem_id}'
            and mem_pass='{mem_pass}'

    """
    print(sql)
    return getview(sql)
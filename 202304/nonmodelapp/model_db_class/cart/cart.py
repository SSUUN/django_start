from nonmodelapp.model_db_class import db_sql


def cartList(col=None,desc=0):

    sql="""
        select cart_member,cart_no,cart_prod,cart_qty
        from cart
        """
    if col:
        sql+=f"order by {col}"
    if desc=="1":
        sql+=f" desc"
    print(sql)
    return db_sql.getList(sql)


def cartView(cart_no,cart_prod):
    sql=f"""
        select cart_member,cart_no,cart_prod,cart_qty
        from cart
        where cart_no='{cart_no}'
            and cart_prod='{cart_prod}'
         """
    return db_sql.getView(sql)


def cartUpdate(cart_no,cart_prod,cart_qty):
    sql=f"""
        update cart
            set cart_qty={cart_qty}
            where cart_no='{cart_no}'
                and cart_prod='{cart_prod}'
        """
    return db_sql.setCUD(sql)


def cartDelete(cart_no,cart_prod):
    sql=f"""
        delete from cart
            where cart_prod='{cart_prod}'
            and cart_no='{cart_no}'

        """
    return db_sql.setCUD(sql)

def cartInsert(cart_no,cart_member,cart_qty,cart_prod):
    sql=f"""
        insert into cart(cart_no,cart_member,cart_qty,cart_prod)
            values('{cart_no}','{cart_member}',{cart_qty},'{cart_prod}')
        """
    return db_sql.setCUD(sql)




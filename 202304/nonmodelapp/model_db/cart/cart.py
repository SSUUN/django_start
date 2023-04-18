from nonmodelapp.model_db import db_sql


def cartList():
    sql="""
        select cart_member,cart_no,cart_prod,cart_qty
        from cart
        """
    return db_sql.getList(sql)

def cartView(cart_no):
    sql=f"""
        select cart_member,cart_no,cart_prod,cart_qty
        from cart
        where cart_no='{cart_no}'
        """
    return db_sql.getView(sql)


def cartUpdate(cart_no,cart_qty):
    sql=f"""
        update cart
            set cart_qty={cart_qty}
            where cart_no='{cart_no}'
        """
    return db_sql.setUpdate(sql)


def cartDelete(cart_no,cart_prod):
    sql=f"""
        delete from cart
            where cart_prod='{cart_prod}'
            and cart_no='{cart_no}'
        """
    return db_sql.setUpdate(sql)

def cartInsert(cart_no,cart_member,cart_qty,cart_prod):
    sql=f"""
        insert into cart(cart_no,cart_member,cart_qty,cart_prod)
            values('{cart_no}','{cart_member}',{cart_qty},'{cart_prod}')
        """
    return db_sql.setUpdate(sql)




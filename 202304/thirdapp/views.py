from django.shortcuts import render
from django.http import HttpResponse
from thirdapp.model_db_class.cart_mem import cart_mem as cmdb
# Create your views here.


def index(request):

    return render(request,"thirdapp/index.html")

def cartmemlist(request):
    re=eval("request."+request.method)
    col=re.get("col")
    desc=re.get("desc")
    print(re)
    cart_mem=cmdb.cart_mem_list(col=col,
                                desc=desc)
    print(cart_mem[0].keys())

    
    return render(request,"thirdapp/cart/cart_mem_list.html",
                  {"cart_mem":cart_mem,
                   "cart_mem_keys":list(cart_mem[0].keys())})


def cartmemview(request):
    re=eval("request."+request.method)

    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    
    
    cart_mem_view=cmdb.cart_mem_view(cart_no=cart_no,
                            cart_prod=cart_prod)
    
    return render(request,"thirdapp/cart/cart_mem_view.html",
                  cart_mem_view)

def cartmemupdateform(request):
    re=eval("request."+request.method)

    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")

    cart_mem_view=cmdb.cart_mem_view(cart_no=cart_no,
                            cart_prod=cart_prod)
    
    return render(request,"thirdapp/cart/cart_mem_update_form.html",
                  cart_mem_view)

def cartmemupdate(request):
    re=eval("request."+request.method)

    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    cart_qty=re.get("cart_qty")

    cmdb.cart_mem_update(cart_no=cart_no,
                            cart_prod=cart_prod,
                            cart_qty=cart_qty)
    msg=f"""
        <script type="text/javascript">
            alert("수정ㅇㅘㄴ료")
            location.href="/third/cartmemview/?cart_no={cart_no}&cart_prod={cart_prod}"
        </script>
        """
    return HttpResponse(msg)

def cartmemdelete(request):
    re=eval("request."+request.method)

    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    #cart_qty=re.get("cart_qty")

    cmdb.cart_mem_delete(cart_no=cart_no,
                            cart_prod=cart_prod,
                            )
    msg=f"""
        <script type="text/javascript">
            alert("수정ㅇㅘㄴ료")
            location.href="/third/cartmemlist"
        </script>
        """
    return HttpResponse(msg)

def cartmeminsertform(request):
    re=eval("request."+request.method)
    mem_id=re.get("mem_id")
    

    mem_view,cart_prod=cmdb.cart_mem_insert_form(mem_id=mem_id)
    mem_view.update({"cart_prod":cart_prod})
    print(cart_prod)
    return render(request,"thirdapp/cart/cart_mem_insert_form.html",
                  mem_view)

def cartmeminsert(request):
    re=eval("request."+request.method)
    mem_id=re.get("mem_id")
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    cart_qty=re.get("cart_qty")
    print(re)
    cart_no=cmdb.cart_mem_insert(mem_id=mem_id,
                         cart_prod=cart_prod,
                         cart_qty=cart_qty)
    print(cart_no)
    msg=f"""
        <script type="text/javascript">
            alert("추가ㅇㅘㄴ료")
            location.href="/third/cartmemview/?cart_no={cart_no}&cart_prod={cart_prod}"
        </script>
        """
    return HttpResponse(msg)


def login_form(request):
    re=eval("request."+request.method)
    mem_id=re.get("mem_id")
    mem_pass=re.get("mem_pass")

    mem_ciew=cmdb.login_fprm(mem_id=mem_id,
                    mem_pass=mem_pass)
    if mem_ciew:
        request.session["mem_id"]=mem_id
        request.session["mem_name"]=mem_ciew["mem_name"]
        msg=f"""
        <script type="text/javascript">
            alert("로그인")
            location.href="/third/cartmemlist"
        </script>
        """
    else:
        msg=f"""
        <script type="text/javascript">
            alert("에러")
            location.href="/third/cartmemlist"
        </script>
        """
    return HttpResponse(msg)

def logout(request):
    request.session.flush()
    
    msg=f"""
    <script type="text/javascript">
        alert("로그아웃")
        location.href="/third/cartmemlist"
    </script>
    """
    return HttpResponse(msg)
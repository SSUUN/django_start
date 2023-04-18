from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def diczip(x,*t):
    for i in t:
        x.update(i)
        
    return x
  
def index(request):
    #return HttpResponse("w")
    return render(request,"oracleapp/index.html")

## 회원정보 전체 조회하기 
def getmemberlist(request):
    # orm방식 전체조회 
    # select * from member
    #all전체조회
    #print(Member.objects.all())
    mem_list=Member.objects.all()
    print()
    print((list(mem_list)[-1]))
    print(len(list(mem_list)))
    return render(request,"oracleapp/member/mem_list.html",
                  {"mem_list":mem_list})



def getmemberview(request):

    mem_id1=request.GET.get("mem_id","ERROR")

    """select * 
    from member
    where mem_id={men_id}"""
    # 모델처리하기(M) 한건조회 
    print(mem_id1)
    #a=Member.objects.all()

    print(Member.objects.all())
    try:

        mem_view=Member.objects.get(mem_id=mem_id1)
    except:
        msg="""
        <script type='text/javascript'>
            alert('잘못된접근')
            location.href="/"
        </script>
        
        """
        return HttpResponse(msg)
    print(mem_view)
    return render(request,"oracleapp/member/mem_view.html",
                  {"mem_view":mem_view})




def getmemberview2(request):
    a=request.GET
    mem_list=Member.objects.all()
    for i in mem_list:
        print(i)
        if a["mem_id"]==i.mem_id:
            return render(request,"oracleapp/member/mem_view.html",{"mem_view":i})
        


def getmemupdateform(request):
    #1.전송 데이터가 있으면 받기
    #2.db입력/수정삭제 조회시 models.py처리
    #3.db처리결과있으면 html 넘겨주기
    mem_id=request.GET.get("mem_id","ERROR")

    try:

        mem_view=Member.objects.get(mem_id=mem_id)
    except:
        msg="""
        <script type='text/javascript'>
            alert('잘못된접근')
            location.href="/"
        </script>
        
        """
        return HttpResponse(msg)
    print(mem_view.mem_id)
    return render(request,"oracleapp/member/mem_update_form.html",{"mem_view":mem_view})


def getmemupdate(request):
    mem_view=request.POST
    print(mem_view)
    mem_id=mem_view.get("mem_id")
    mem_pass=mem_view.get("mem_pass")
    mem_add1=mem_view.get("mem_add1")
    
    if not mem_view.get("mem_id"):

        
        msg="""
        <script type='text/javascript'>
            alert('잘못된접근')
            location.href="/"
        </script>
        
        """
        return HttpResponse(msg)
    
    """ update member 
            set mem_pass={mem_pass},
                mem_add1={mem_add1}
        where mem_id={mem_id}"""

    Member.objects.filter(mem_id=mem_id).update(mem_pass=mem_pass,
                                                mem_add1=mem_add1)
    msg=f"""<script type='text/javascript'>
            alert('수정완료');
            location.href='/oracle/mem_view/?mem_id={mem_id}';
            </script>
                            
                            '""" 
    return HttpResponse(msg)   

def getmemdelete(request):
    mem_view=request.POST
    print(mem_view)
    mem_id=mem_view.get("mem_id")
    
    

    """ deletr from member 
        where mem_id={mem_id}"""

    Member.objects.filter(mem_id=mem_id).delete()
    msg=f"""<script type='text/javascript'>
            alert('삭제완료');
            location.href='/oracle/mem_view/?mem_id={mem_id}';
            </script>
                            
                            '""" 
    return HttpResponse(msg)   

## cart
def getcartlist(request):
    ## 1. 전달받을 ㅍ라메터 있으면 받기 get,post
    ## 2. model에사 crud 처리할게 있으면 처리하기
    ## 3. temmplates :html 생성
    ## 4. model 을 html 에 넘기기 :return render()
    cart_list=Cart.objects.all()
    re=eval("request."+request.method)
    col=re.get("col","error")
    desc=re.get("desc","error")
    cart_list=Cart.objects.all()
    if col!="error":
        s=""
        if desc=="0":
            s+="-"
        s+=col
        cart_list=cart_list.order_by(s)
    return render(request,"oracleapp/cart/cart_list.html",
                  {"cart_list":cart_list})
## cart
def getcartview(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")

    print(dict(re))
    """
     select * 
     from cart
      where cart_prod=cart_prod
        and cart_no=cart_no
          """
    try:
        cart_list=Cart.objects.values().get(cart_prod=cart_prod,
                               cart_no=cart_no)
        
    except:
        msg="""
        <script type='text/javascript'>
            alert('잘못된접근')
            location.href="/"
        </script>
        
        """
        return HttpResponse(msg)
    
    print(cart_list)
    return render(request,"oracleapp/cart/cart_view.html",
                  cart_list)


def getupdateform(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    try:

        cart_list=Cart.objects.values().get(cart_prod=cart_prod,
                               cart_no=cart_no)
    except:
        msg="""
        <script type='text/javascript'>
            alert('잘못된접근')
            location.href="/"
        </script>
        
        """
        return HttpResponse(msg)
    print(cart_list)
    return render(request,"oracleapp/cart/update_form.html",
                  cart_list)



def getcartupdate(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    cart_qty=re.get("cart_qty")

    Cart.objects.filter(cart_no=cart_no,
                        cart_prod=cart_prod
                        ).update(cart_qty=cart_qty)
    
    msg=f"""
    <script type="text/javascript">
        alert("수정완료");
        location.href="/oracle/cart_view/?cart_no={cart_no}&cart_prod={cart_prod}";
    </script>

    """
    return HttpResponse(msg)


def getCartDelete(request):
    re=eval("request."+request.method)

    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")


    Cart.objects.filter(cart_no=cart_no,
                        cart_prod=cart_prod
                        ).delete()
    
    msg=f"""
    <script type="text/javascript">
        alert("삭제완료");
        location.href="/oracle/cart_list/";
    </script>

    """
    return HttpResponse(msg)


def getcartinsertform(request):
    return render(request,"oracleapp/cart/cart_insert_form.html")

def getcartinsert(request):
    re=eval("request."+request.method)
    #for i in re.keys():
        #eval(f"{i}=re.get({i})")
    cart_member=re.get("cart_member")
    cart_prod=re.get("cart_prod")
    cart_no=re.get("cart_no")
    cart_qty=re.get("cart_qty")
    print(123123123)
    print(re)
    try:
        Cart.objects.create(cart_no=cart_no,
                            cart_prod=cart_prod,
                            cart_member_id=cart_member,
                            cart_qty=cart_qty)
    except Exception as e:
        if "unique" in str(e):
            msg=f"""
            <script type="text/javascript">
                alert("중복에러");
                history.go(-1);
            </script>

            """
            return HttpResponse(msg)
    
    
    msg=f"""
    <script type="text/javascript">
        alert("저장완료");
        location.href="/oracle/cart_view/?cart_no={cart_no}&cart_prod={cart_prod}";
    </script>

    """

    return HttpResponse(msg)


def getmemcartlist(request):



    cart_list=Cart.objects.all()
    re=eval("request."+request.method)
    col=re.get("col","error")
    desc=re.get("desc","error")
    cart_list=Cart.objects.all()
    if col!="error":
        s=""
        if desc=="0":
            s+="-"
        s+=col
        cart_list=cart_list.order_by(s)
    zip(map(lambda x:x.cart_member.__dict__,cart_list),
        map(lambda x:x.__dict__,cart_list))

    def diczip(x,y):
        x.update(y)
        return x
    cart_list1=list(map(lambda x:diczip(x.cart_member.__dict__,x.__dict__),cart_list))
    print(cart_list1)
    
    return render(request,"oracleapp/mem_cart/mem_cart_list.html",
                  {"cart_list":cart_list1})


## cart
# def getmcartlist(request):
#     ## 1. 전달받을 ㅍ라메터 있으면 받기 get,post
#     ## 2. model에사 crud 처리할게 있으면 처리하기
#     ## 3. temmplates :html 생성
#     ## 4. model 을 html 에 넘기기 :return render()

#     cart_list=Cart.objects.all()
#     return render(request,"oracleapp/mem_cart/cart_list.html",
#                   {"cart_list":cart_list})
## cart
def getmcartview(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    print(dict(re))
    """
     select * 
     from cart
      where cart_prod=cart_prod
        and cart_no=cart_no
          """
    #Cart.objects.select_related().filter(mem_id=)
    
    cart_list=Cart.objects.get(cart_prod=cart_prod,
                               cart_no=cart_no)
    cart_list1=cart_list.cart_member.__dict__
    cart_list1.update(cart_list.__dict__)

    return render(request,"oracleapp/mem_cart/cart_view.html",
                  cart_list1)


def getmupdateform(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    cart_list=Cart.objects.values().get(cart_prod=cart_prod,
                               cart_no=cart_no)
    print(cart_list)
    return render(request,"oracleapp/mem_cart/update_form.html",
                  cart_list)



def getmcartupdate(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    cart_qty=re.get("cart_qty")

    Cart.objects.filter(cart_no=cart_no,
                        cart_prod=cart_prod
                        ).update(cart_qty=cart_qty)
    
    msg=f"""
    <script type="text/javascript">
        alert("수정완료");
        location.href="/oracle/mem_cart_view/?cart_no={cart_no}&cart_prod={cart_prod}";
    </script>

    """
    return HttpResponse(msg)


def getmCartDelete(request):
    re=eval("request."+request.method)

    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")


    Cart.objects.filter(cart_no=cart_no,
                        cart_prod=cart_prod
                        ).delete()
    
    msg=f"""
    <script type="text/javascript">
        alert("삭제완료");
        location.href="/oracle/mem_cart_list/";
    </script>

    """
    return HttpResponse(msg)


def getmcartinsertform(request):
    return render(request,"oracleapp/mem_cart/cart_insert_form.html")

def getmcartinsert(request):
    re=eval("request."+request.method)
    cart_member_id=re.get("cart_member_id")
    cart_prod=re.get("cart_prod")
    cart_no=re.get("cart_no")
    cart_qty=re.get("cart_qty")
    print(re)

    Cart.objects.create(cart_no=cart_no,
                        cart_prod=cart_prod,
                        cart_member_id=cart_member_id,
                        cart_qty=cart_qty)
    msg=f"""
    <script type="text/javascript">
        alert("저장완료");
        location.href="/oracle/mem_cart_view/?cart_no={cart_no}&cart_prod={cart_prod}";
    </script>

    """

    return HttpResponse(msg)


def getmemview(request):
    re=eval("request."+request.method)
    cart_member_id=re.get("cart_member_id")

    #cart_list2=Cart.objects.distinct("cart_member_id")
    #.get(cart_member_id=cart_member_id)

    mem_list=Cart.objects.filter(cart_member_id=cart_member_id).first()
    #mem_list=Cart.objects.get(cart_member_id=cart_member_id)
    #Cart.objects
    print(mem_list)
    

    # Menber
    cart_list1=mem_list.cart_member.__dict__ 

    # Cart 
    #cart_list1.update(mem_list.__dict__)

    print(mem_list)
    return render(request,
                  "oracleapp/mem_cart/mem_view.html",
                  cart_list1)


def getProdList(request):
    re=eval("request."+request.method)

    col=re.get("col","error")
    desc=re.get("desc","error")
    kk=re.get("kk",0)

    prod_list=Prod.objects.all()
    if col!="error":
        s=""
        if desc=="0":
            s+="-"
        s+=col
        prod_list=prod_list.order_by(s)
    #prod_list=Prod.objects.all()
    
    

    return render(request,"oracleapp/prod/prod_list.html",
                  {"prod_list":prod_list,
                   "kk":int(kk)})
                  

def getProdView(request):
    re=eval("request."+request.method)
    
    prod_id=re.get("prod_id")

    prod_list=Prod.objects.values().get(prod_id=prod_id)
    print(prod_list)
    return render(request,"oracleapp/prod/prod_view.html",
                  prod_list)


def getProdUpdateForm(request):

    re=eval("request."+request.method)
    prod_id=re.get("prod_id")

    prod_list=Prod.objects.values().get(prod_id=prod_id)


    return render(request,"oracleapp/prod/prod_update_form.html",
                  prod_list)

def getProdUpdate(request):
    re=eval("request."+request.method)
    prod_id=re.get("prod_id")
    prod_name=re.get("prod_name")
    prod_cost=re.get("prod_cost")
    prod_price=re.get("prod_price")
    prod_sale=re.get("prod_sale")

    Prod.objects.filter(prod_id=prod_id).update(prod_name=prod_name,
                                                prod_cost=prod_cost,
                                                prod_price=prod_price,
                                                prod_sale=prod_sale,
                                                )
    
    msg=f"""
        <script type='text/javascript'>
            alert('수정완료')
            location.href="/oracle/prod_view/?prod_id={prod_id}"
        </script>"""
    return HttpResponse(msg)

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import os
# Create your views here.
def diczip(x,*t):
    for i in t:
        x.update(i)
    return x

def index(request):
    return render(request,
                  "secondapp/index.html")



def second(request):
    #return HttpResponse("second 호출")
    return render(request,
                  "secondapp/index.html")
 

def getmemberall(request):
    a=Member.objects
    a1=a.all()
    print(123,a.count())
    return render(request,"secondapp/member/mem_all.html",
                  {"a":a1})


def get_view(request):
    mem_id=request.GET.get("mem_id","error")
    mem_view=Member.objects.get(mem_id=mem_id)
    
    return render(request,"secondapp/member/mem_view.html",
                  {"mem_view":mem_view})


def get_update_form(request):
    mem_id=request.GET.get("mem_id","error")
    print(123123123123,mem_id)
    mem_view=Member.objects.get(mem_id=mem_id)
    
    return render(request,"secondapp/member/mem_update_form.html",
                  {"mem_view":mem_view})

def get_update(request):
    re=request.POST
    mem_id=re.get("mem_id","error")
    mem_pass=re.get("mem_pass","error")
    mem_add1=re.get("mem_add1","error")
    mem_name=re.get("mem_name","error")
    print(mem_id,mem_pass,mem_add1)
    Member.objects.filter(mem_id=mem_id).update(mem_pass=mem_pass,
                                                mem_add1=mem_add1,
                                                mem_name=mem_name)
    msg=f"""<script type='text/javascript'>
            alert('수정완료');
            location.href='/second/mem_view/?mem_id={mem_id}';
            </script>
 '""" 
    return HttpResponse(msg)

def getcartlist(request):
    re=eval("request."+request.method)
    col=re.get("col","error")
    desc=re.get("desc","error")
    cart_list=Cart.objects.all()
    if col!="error":
        s=""
        if desc=="0":
            s+="-"
        s+=col
        cart_list=cart_list.order_by(s)
    
    return render(request,"secondapp/cart/cart_list.html",
                  {"cart_list":cart_list})

def getcartview(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")

    cart_list=Cart.objects.values().get(cart_no=cart_no,
                                cart_prod=cart_prod)
    return render(request,"secondapp/cart/cart_view.html",
                  cart_list)

def getcartupdateform(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")

    cart_list=Cart.objects.values().get(cart_no=cart_no,
                              cart_prod=cart_prod)
    
    return render(request,"secondapp/cart/cart_update_form.html",cart_list)

def getcartupdate(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    cart_qty=re.get("cart_qty")
    Cart.objects.filter(cart_no=cart_no,
                                cart_prod=cart_prod).update(cart_qty=cart_qty)

    msg=f"""
        <script type='text/javascript'>
            alert('수정완료')
            location.href='/second/cart_view/?cart_no={cart_no}&cart_prod={cart_prod}'
        </script>
        """

    return HttpResponse(msg)

def getcartdelete(request):
    re=eval("request."+request.method)
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    Cart.objects.filter(cart_no=cart_no,
                        cart_prod=cart_prod).delete()
    
    msg="""
        <script type='text/javascript'>
            alert('삭제완료')
            location.href='/second/cart_list/'
        </script>
    """
    return HttpResponse(msg)

def getcartinsertform(request):
    return render(request,"secondapp/cart/cart_insert_form.html")

def getcartinsert(request):
    re=eval("request."+request.method)
    
    cart_member=re.get("cart_member")
    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")
    cart_qty=re.get("cart_qty")

    Cart.objects.create(cart_member=cart_member,
                        cart_no=cart_no,
                        cart_prod=cart_prod,
                        cart_qty=cart_qty)
    msg=f"""
        <script type='text/javascript'>
            alert('저장완료')
            location.href='/second/cart_view/?cart_no={cart_no}&cart_prod={cart_prod}'
        </script>
    """
    return HttpResponse(msg)


def getCartMemberProdList(request):

    # lprod_list=Lprod.objects.values()
    # buyer_list=Buyer.objects.values()
    # buyprod_list=Buyprod.objects.values()
    # prod_list=Prod.objects.values()
    # cart_list=Cart.objects.values()
    # member_list=Member.objects.values()

    cart_list2=Cart.objects.all()
    cart_list2=list(map(lambda x:diczip(x.cart_member.__dict__,
                    x.cart_prod.__dict__,
                    x.__dict__),cart_list2))
    
    print(cart_list2)
    cart_list2
    cart_list23=list(map(lambda x:list(x.values())[1:],cart_list2))

    return render(request,"oracleapp/cart_mem_prod/cart_mem_prod.html",
                  {"cart_list2":cart_list2,
                   "cart_list_key":list(cart_list2[0].keys())[1:],
                   "cart_list_values":cart_list23,})

def getCartMemberProdList1(request):

    cart_list2=Cart.objects.all()
    cart_list2=list(map(lambda x:diczip(x.cart_member.__dict__,
                    x.cart_prod.__dict__,
                    x.__dict__),cart_list2))
    
  
    cart_list23=list(map(lambda x:list(x.values())[1:],cart_list2))

    return render(request,"oracleapp/cart_mem_prod/all_list.html",
                  {"cart_list2":cart_list2,
                   "cart_list_key":list(cart_list2[0].keys())[1:],
                   "cart_list_values":cart_list23,})
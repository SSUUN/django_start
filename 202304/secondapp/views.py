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


def allTest(request):

    lprod_list=Lprod.objects.values()
    buyer_list=Buyer.objects.values()
    buyprod_list=Buyprod.objects.values()
    prod_list=Prod.objects.values()
    cart_list=Cart.objects.values()
    member_list=Member.objects.values()
    car=Cart.objects.all()[0]
    cart_list2=list(map(lambda x:diczip(x.cart_member.__dict__,
                    x.cart_prod.__dict__,
                    x.__dict__),Cart.objects.all()))
    
    print(cart_list2)

    return render(request,"secondapp/all/all_test.html",
                  {"lprod_list":lprod_list,
                   "buyer_list":buyer_list,
                  "buyprod_list":buyprod_list ,
                   "prod_list":prod_list,
                   "cart_list":cart_list,
                   "member_list":member_list,
                   "all":[lprod_list,
                          buyer_list,
                          buyprod_list,
                          prod_list,
                          cart_list,
                          member_list],
                    "car":car.cart_member.__dict__,
                    "cart_list2":cart_list2})
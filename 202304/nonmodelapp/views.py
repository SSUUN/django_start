from django.shortcuts import render

from django.shortcuts import HttpResponse

from nonmodelapp.model_db_class.member import member
from nonmodelapp.model_db_class.cart import cart

# Create your views here.
def index(request):
    return render(request,"nonmodelapp/index.html")


def getMemberList(request):
    sql=f"""
        select mem_id,mem_pass,mem_name,mem_add1
        from member
        """
    mem_list=member.getMemberList1()
    #print(mem_list)
    return render(request,"nonmodelapp/member/mem_list.html",
                  {"mem_list":mem_list})


def getmemberview(request):
    mem_id1=request.GET.get("mem_id","a001")
    try:
        mem_view=member.getMember(mem_id=mem_id1)
    except:

        msg="""
        <script type='text/javascript'>
            alert('잘못된접근')
            location.href="/"
        </script>
        """
        return HttpResponse(msg)
    print(mem_view)
    return render(request,"nonmodelapp/member/mem_view.html",
                  {"mem_view":mem_view})


def getMemberUpdateform(request):
    mem_id1=request.GET.get("mem_id","a001")
    print(mem_id1)
    mem_view=member.getMember(mem_id=mem_id1)

    #print(mem_list)
    return render(request,"nonmodelapp/member/mem_update_form.html",
                  {"mem_view":mem_view})

def getMemberUpdate(request):
    re=eval("request."+request.method)
    mem_id=re.get("mem_id","a001")
    mem_pass=re.get("mem_pass","a001")
    mem_add1=re.get("mem_add1","a001")

    print(mem_id)
    mem_view=member.getMemberUpdate(mem_id=mem_id,
                                    mem_pass=mem_pass,
                                    mem_add1=mem_add1)

    #print(mem_list)
    msg=f"""
        <script type='text/javascript'>
            alert('수정완료')
            location.href='/nonmodel/mem_view/?mem_id={mem_id}'
        </script>
            """
    return HttpResponse(msg)
    return render(request,"nonmodelapp/member/mem_update_form.html",
                  {"mem_view":mem_view})



###cart

def getCartList(request):
    re=eval("request."+request.method)
    col=re.get("col")
    desc=re.get("desc")
    print(desc)
    cart_list=cart.cartList(col=col,
                            desc=desc)

    #print(mem_list)
    return render(request,"nonmodelapp/cart/cart_list.html",
                  {"cart_list":cart_list})


def getCartview(request):
    cart_no=request.GET.get("cart_no","a001")
    cart_prod=request.GET.get("cart_prod","a001")
    try:
        cart_view=cart.cartView(cart_no=cart_no,
                                cart_prod=cart_prod)
    except:

        msg="""
        <script type='text/javascript'>
            alert('잘못된접근')
            location.href="/"
        </script>
        """
        return HttpResponse(msg)
    print(cart_view)
    return render(request,"nonmodelapp/cart/cart_view.html",
                  cart_view)


def getCartUpdateform(request):
    cart_no=request.GET.get("cart_no","a001")
    cart_prod=request.GET.get("cart_prod","a001")
    #print(mem_id1)
    cart_view=cart.cartView(cart_no=cart_no,
                            cart_prod=cart_prod)

    #print(mem_list)
    return render(request,"nonmodelapp/cart/update_form.html",
                  cart_view)

def getCartUpdate(request):

    re=eval("request."+request.method)

    cart_no=re.get("cart_no","a001")
    cart_qty=re.get("cart_qty","a001")
    cart_prod=re.get("cart_prod","a001")
    #mem_add1=re.get("mem_add1","a001")

    mem_view=cart.cartUpdate(cart_no=cart_no,
                             cart_prod=cart_prod,
                            cart_qty=cart_qty
                                    )

    #print(mem_list)
    msg=f"""
        <script type='text/javascript'>
            alert('수정완료')
            location.href='/nonmodel/cart_view/?cart_no={cart_no}&cart_prod={cart_prod}'
        </script>
            """
    return HttpResponse(msg)
    return render(request,"nonmodelapp/member/mem_update_form.html",
                  {"mem_view":mem_view})




def getCartDelete(request):
    re=eval("request."+request.method)

    cart_no=re.get("cart_no")
    cart_prod=re.get("cart_prod")


    cart.cartDelete(cart_no=cart_no,
                        cart_prod=cart_prod
                        )
    
    msg=f"""
    <script type="text/javascript">
        alert("삭제완료");
        location.href="/nonmodel/cart_list/";
    </script>

    """
    return HttpResponse(msg)


def getcartinsertform(request):
    return render(request,"nonmodelapp/cart/cart_insert_form.html")

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
        cart.cartInsert(cart_no=cart_no,
                            cart_prod=cart_prod,
                            cart_member=cart_member,
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
        location.href="/nonmodel/cart_view/?cart_no={cart_no}&cart_prod={cart_prod}";
    </script>

    """

    return HttpResponse(msg)


## login 


def login_form(request):
    return render(request,"nonmodelapp/login_form.html")



def login_chk(request):
    re=eval("request."+request.method)
    mem_id=re.get("mem_id")
    mem_pass=re.get("mem_pass")
    
    l=member.getloginChk(mem_id=mem_id,
                       mem_pass=mem_pass)
    print(l)

    if not l.get("RS"):
        msg=f"""
                <script type='text/javascript'>
                alert('{l["mem_name"]} 로그인')
                    location.href="/nonmodel/index/"
                </script>
            """
        # 로그인 상태 유지하기 위한 세션 처리
        # reques 객체내에 존재하는 session 변수를 사용해서
        # 서버영ㅇ역에 값을 저장해놓는기능
        # 사용자가 로그아웃 또는 브라우져를 종횰하면 서버좁석 끊어자고
        # 이때 세션 삭제된다 
        # session 변수는 딕셔너리타입의 변수로 key,value
        # request 객테는 어디서든 사용가능 
        
        request.session["ses_mem_id"]=mem_id
        request.session["ses_mem_name"]=l.get("mem_name")
        
    else:
        msg="""
                <script type='text/javascript'>
                    alert("에러")
                    location.href="/nonmodel/login_form/"
                </script>
            """
    
    return HttpResponse(msg) 


def logout_chk(request):
    # 로그아웃의 의미 session 정보 삭재
    request.session.flush()
    msg=f"""
        <script type="text/javascript">
            alert("로그아웃")
            location.href='/nonmodel/index/'
        </script>"""
    return HttpResponse(msg)
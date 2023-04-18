from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"frontapp/index.html",)

def imageview(request):
    return render(request,"frontapp/01_image.html")

def cssview1(request):
    return render(request,"frontapp/02_css1.html")
def cssview2(request):
    return render(request,"frontapp/02_css2.html")
def cssview3(request):
    return render(request,"frontapp/02_css3.html")
def csstestview(request):
    return render(request,"frontapp/css_test.html")

def javascriptview1(request):
    return render(request,"frontapp/01_javasceipt1.html")
def javascriptview2(request):
    return render(request,"frontapp/01_javasceipt2.html")
def javascriptview3(request):
    return render(request,"frontapp/01_javasceipt3.html")

def htmlview01(request):
    return render(request,"frontapp/html/01_html.html")


def linkview(request):
    return render(request,"frontapp/html/02_link.html")
def linkview2(request):
    return render(request,"frontapp/html/03_link.html")

def cssview(request):
    return render(request,"frontapp/html/04_css.html")

def tableview(request):
    return render(request,"frontapp/html/05_table.html")
def tableview2(request):
    context={"id":"a001",
                    "name":"홍길동",
                    "addres":"광주광역시 소촌동"}
    yy=[[1,2,4]]*10
    return render(request,
                  "frontapp/html/06_table.html",
                  {"id":[context]*1,
                   "q":yy})

def ulview(request):
    return render(request,"frontapp/html/07_ul.html")
def divview(request):
    return render(request,
                  "frontapp/html/08_div.html")
def divview2(request):
    return render(request,
                  "frontapp/html/09_div.html")

def iframeview(request):
    return render(request,
                  "frontapp/html/10_iframe.html")

def csstableview(request):
    return render(request,
                  "frontapp/css/01_table.html")
def csstableview2(request):
    return render(request,
                  "frontapp/css/02_table.html")
def cssnavview(r):
    return render(r,
                  "frontapp/css/03_nav.html")


def jsinputfromview(request):
    return render(request,
                  "frontapp/js/01_inputfrom.html",
                  {"no":"10",
                   "mem_id":"a123",
                   "mem_pw":"1234",
                   })
## 입력폼에서 넘어온ㄴ 값 처리
# 브라우저 url 에 입력해서 들어오면 안됨
#오류원인 전달받는 값이 없어서 
# 입려곰을통ㅎ서
def jslogin(request):
    # 요청순서 
    #1. 요청데이터 받기
    # 전송방식에 따라 구분하여 받기 : 조건처리
    # 모든 데이터는 딕셔너리 타입으로 전송됨
    # POST , GET 는 딕셔너리 변수가 됨
    
    """if request.method=="POST":
        a=request.POST
    elif request.method=="GET":
        a=request.GET"""
    
        #no=request.POST["no"]
        #mem_id=request.POST["mem_id"]
        #mem_pw=request.POST["mem_pw"]
    
        #no=request.GET["no"]
        #mem_id=request.GET["mem_id"]
        #mem_pw=request.GET["mem_pw"]


    #a=dict(a)
    #2. 요청 에이터이용 db 처리
    # 임의 테이블 있다고 가정 
    # 컬럼은 p_id p_pw 있다고 가정 
    a=eval("request."+request.method)
    p_id="a001"
    p_pw="asdf"
    # 전송받은 아이디와 pw 가 같다면 모두 응답처리
    # 둘중 하나라도 다르다면 응답메세지 아이디또는 ㅐ스워드가 같지않습니다
    #3. db 처리결과 응답하기 html또는 메세지"""

    """
    select p_id ,p_pw from textTB
    where p_id = a["mem_id"]
    and p_pw = a["mem_pw"]
   
   
    insert into textTB (a,b,c)
    values (a["mem_id"],a["mem_pw"],a["no"])


    uptate testTB
        set no=a["no"]
        where p_id = a["mem_id"]


    delete from testTB
    where p_id = a["mem_id"]
        and p_pw = a["mem_pw"]
    """

    if (a["mem_id"],a["mem_pw"])==(p_id ,p_pw) :
        rs_msg="""
            <script type='text/javascript'>
                alert('정상적 로그인 되었습니다!!');
                location.href='/front/';
            </script>
        """
    else:
        rs_msg="""
            <script type='text/javascript'>
                alert('비정상적 로그인 되었습니다!!');
                history.go(-1);
            </script>
        """

    
    return HttpResponse(rs_msg)


def radiobuttonview(request):
    return render(request,
                  "frontapp/js/03_radiobutton.html",
                )

def jsradio_back(request):
    a =dict(eval("request."+request.method))
    if not a.get("city"):
        re_msg=f"""<script type='text/javascript'>
                    alert('지역을 선택하세요');
                    history.go(-1);
                </script>
                """
    else:
        re_msg=f"""<h1>{request.method} {a['city'][0]} <h1>"""
    return HttpResponse(re_msg)

def jsradio(request):
    # 여기서 가져온건 그냥 딕셔너리에 좀이상함 "value"
    # 파이썬으로 바꾸면 리스트 안으로 들어감 ["value"]
    try:
        a =dict(eval("request."+request.method))
        print(a)
        if not a.get("city"):
            re_msg=f"""<script type='text/javascript'>
                        alert('지역을 선택하세요');
                        history.go(-1);
                        </script>
                    """
        else:
            print(",".join(a['city']))
            re_msg=f"""<h1>{request.method} {a['city']} <h1>"""
    except:
        return HttpResponse("<h1>접근에러<h1>")
    
    return HttpResponse(re_msg)
    

def checkboxview(request):
    area1="광주"
    area="광주,서울,경기"
    return render(request,"frontapp/js/05_checkbox.html",
                  {"area":area,
                   "area1":area1})


def selectboxview(request):
    area="광주"
    area="광주,서울,경기"
    return render(request,
                  "frontapp/js/06_selectbox.html",
                  {"area":area})

def requiredview(request):
    return render(request,
                  "frontapp/js/07_input_required.html")
def requiredview2(request):
    return render(request,
                  "frontapp/js/08_input_required.html")

def jqueryview1(request):
    return render(request,"frontapp/jquery/01_jquery.html")

def slidejquery(request):
    return render(request,"frontapp/jquery/02_slidejquery.html")

def bootstrap01(request):
    return render(request,"frontapp/bootstrap/01_bootstrap.html")
def bootstrap_table(request):
    return render(request,"frontapp/bootstrap/02_bootstrap_table.html")

def bootstrap_form(request):
    return render(request,"frontapp/bootstrap/03_bootstrap_form.html")
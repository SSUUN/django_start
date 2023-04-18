from django.shortcuts import render

## 사용자 브라우저로 응답을 하기우한 라이브러리
from django.shortcuts import HttpResponse

# Create your views here.

def testpage(request):
    return HttpResponse("django ok")

## 최초페이지
def index(request):
    msg=""" 
        <h1> index page 입니다.<h1>
        <hr/>
        <p>
            html 코드 잘 실행됩니다,
        </p>
        """
    #return HttpResponse(msg)
    return render(request,
                  "firstapp/index.html",
                  {"key":"value잘나오오오오오오옴 d",
                   "key1":"value2잘2222222222222222옴 d",})

def index(request):
    return render(request,
                  "firstapp/index.html",
                  {"key":"value잘나오오오오오오옴 d",
                   "key1":"value2잘2222222222222222옴 d",})
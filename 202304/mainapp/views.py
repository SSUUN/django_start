from django.shortcuts import render

## 사용자 브라우저로 응답을 하기우한 라이브러리
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("a0.... a0....abcdefghijklmnopqrstuvwxyz")
     return render(request,
                   "mainapp/index.html",
                   {},)

def main(request):
    #return HttpResponse("a0.... a0....abcdefghijklmnopqrstuvwxyz")
     return render(request,
                   "mainapp/main.html",
                   {},)
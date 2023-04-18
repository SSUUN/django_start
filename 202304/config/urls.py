"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.http import HttpResponse
from django.contrib import admin
from django.urls import path,include
#from firstapp import views as v1
#from secondapp import views as v2

### https://127.0.0.1:8000/url경로/

### path role  path("url경로",함수이름)
from mainapp import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    #path('index/',include("mainapp.urls")),
    
    # path('second/', v2.second),
    # path('testpage/', v1.testpage),
    #path('',lambda x:HttpResponse(" hi") ),
    path('main/' ,include("mainapp.urls")),
    path('front/' ,include("frontapp.urls")),
    path('first/', include("firstapp.urls")),
    path('second/', include("secondapp.urls")),
    path('third/', include("thirdapp.urls")),
    path('oracle/', include("oracleapp.urls")),
    path('nonmodel/', include("nonmodelapp.urls")),
    path('admin/', admin.site.urls),

]

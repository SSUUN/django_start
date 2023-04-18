
from django.urls import path
from . import views
### https://127.0.0.1:8000/url경로/

### path role  path("url경로",함수이름)

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('testpage/', views.testpage),
    
    ]

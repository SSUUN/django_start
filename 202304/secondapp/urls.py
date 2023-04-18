
from django.urls import path
from . import views
### https://127.0.0.1:8000/url경로/

### path role  path("url경로",함수이름)

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('second/', views.second),
    path('mem_all/', views.getmemberall),
    path('mem_view/', views.get_view),
    path('mem_update_form/', views.get_update_form),
    path('mem_update/', views.get_update),
    path('cart_list/', views.getcartlist),
    path('cart_view/', views.getcartview),
    path('cart_update_form/', views.getcartupdateform),
    path('cart_update/', views.getcartupdate),
    path('cart_delete/', views.getcartdelete),
    path('cart_insert_form/', views.getcartinsertform),
    path('cart_insert/', views.getcartinsert),
    path('all_test/', views.allTest),
    
    ]

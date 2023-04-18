
from django.urls import path
from . import views
### https://127.0.0.1:8000/url경로/

### path role  path("url경로",함수이름)

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('mem_list/', views.getMemberList),
    path('mem_view/', views.getmemberview),
    path('mem_update_form/', views.getMemberUpdateform),
    path('mem_update/', views.getMemberUpdate),
    path('cart_list/', views.getCartList),
    path('cart_view/', views.getCartview),
    path('cart_update_form/', views.getCartUpdateform),
    path('cart_update/', views.getCartUpdate),
    path('cart_insert_form/', views.getcartinsertform),
    path('cart_insert/', views.getcartinsert),
    path('cart_delete/', views.getCartDelete),
    path('login_form/', views.login_form),
    path('login_chk/', views.login_chk),
    path('logout_chk/', views.logout_chk),
    
    ]

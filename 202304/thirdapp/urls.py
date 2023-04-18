
from django.urls import path
from . import views
### https://127.0.0.1:8000/url경로/

### path role  path("url경로",함수이름)

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('cartmemlist/', views.cartmemlist),
    path('cartmemview/', views.cartmemview),
    path('cart_mem_update_form/', views.cartmemupdateform),
    path('cart_mem_update/', views.cartmemupdate),
    path('cart_mem_delete/', views.cartmemdelete),
    path('cart_mem_insert_form/', views.cartmeminsertform),
    path('cart_mem_insert/', views.cartmeminsert),
    path('login_form/', views.login_form),
    path('logout/', views.logout),
    
    
    ]

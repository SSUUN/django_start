
from django.urls import path
from . import views
### https://127.0.0.1:8000/url경로/

### path role  path("url경로",함수이름)

urlpatterns = [
    ### https://127.0.0.1:8000/oracle/
    path('', views.index),
    path('index/', views.index),

    ## 회원 관리

    path('mem_list/', views.getmemberlist),
    path('mem_view/', views.getmemberview),
    path('mem_update_form/', views.getmemupdateform),
    path('mem_update/', views.getmemupdate),
    path('cart_list/', views.getcartlist),
    path('cart_view/', views.getcartview),
    path('cart_update_form/', views.getupdateform),
    path('cart_update/', views.getcartupdate),
    path('cart_delete/', views.getCartDelete),
    path('cart_insert_form/', views.getcartinsertform),
    path('cart_insert/', views.getcartinsert),
    path('mem_cart_list/', views.getmemcartlist),
    path('mem_cart_view/', views.getmcartview),
    path('mem_cart_update_form/', views.getmupdateform),
    path('mem_cart_update/', views.getmcartupdate),
    path('mem_cart_delete/', views.getmCartDelete),
    path('mem_cart_insert_form/', views.getmcartinsertform),
    path('mem_cart_insert/', views.getmcartinsert),
    path('mem_cart_mem_view/', views.getmemview),
    path('prod_list/', views.getProdList),
    path('prod_view/', views.getProdView),
    path('prod_update_form/', views.getProdUpdateForm),
    path('prod_update/', views.getProdUpdate),
    path('cart_mem_prod_list/', views.getCartMemberProdList),
    path('cart_mem_prod_list_all/', views.getCartMemberProdList1),
    ]

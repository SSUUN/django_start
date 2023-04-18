
from django.urls import path
from . import views
### https://127.0.0.1:8000/url경로/

### path role  path("url경로",함수이름)

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('image/', views.imageview),
    path('css_1/', views.cssview1),
    path("css_2/",views.cssview2),
    path("css_3/",views.cssview3),
    path("css_test/",views.csstestview),
    path("javascript1/",views.javascriptview1),
    path("javascript2/",views.javascriptview2),
    path("javascript3/",views.javascriptview3),
    path("01_html/",views.htmlview01),
    path("02_link/",views.linkview),
    path("03_link/",views.linkview2),
    path("04_css/",views.cssview),
    path("05_table/",views.tableview),
    path("06_table/",views.tableview2),
    path("07_ul/",views.ulview),
    path("08_div/",views.divview),
    path("09_div/",views.divview2),
    path("10_iframe/",views.iframeview),
    path("01_csstable/",views.csstableview),
    path("02_csstable/",views.csstableview2),
    path("03_cssnav/",views.cssnavview),
    path("01_jsinputfrom/",views.jsinputfromview),
    path("02_login/",views.jslogin),
    path("03_raciobutton/",views.radiobuttonview),
    path("04_radio/",views.jsradio),
    path("05_checkbox/",views.checkboxview),
    path("06_selectbox/",views.selectboxview),
    path("07_required/",views.requiredview),
    path("08_required/",views.requiredview2),
    path("01_jquery/",views.jqueryview1),
    path("02_slidejquery/",views.slidejquery),
    path("bootstrap01/",views.bootstrap01),
    path("bootstrap_table/",views.bootstrap_table),
    path("bootstrap_form/",views.bootstrap_form),
    ]

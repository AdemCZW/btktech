from django.urls import path
from .views import (
   IndexListView,
   Welding_01View,
   Welding_02View,
   HomeListView,
   cpn_01View,
   mta_01View,
   sys_01View,
   
)

app_name = 'herrmann'
urlpatterns = [
    path('nav', HomeListView, name="home"),
    path('', IndexListView.as_view(), name="index"),
    path('welding', Welding_02View.as_view(), name="weld-2"),
    path('components', cpn_01View.as_view(), name="cpn"),
    path('metal', mta_01View.as_view(), name="mta")
    path('system', sys_01View.as_view(), name="sys")
   
   
]
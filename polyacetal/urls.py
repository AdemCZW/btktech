from django.urls import path, re_path
from . import views
from rest_framework import routers
from django.views.generic import TemplateView
from .views import (
    DetailAPIview,
    ListCreateAPIView,
    ListCreateAPIView_ffmm_page,
    DetailAPIview_ffmm_page,
    ListCreateAPIView_bcm_page,
    DetailAPIview_bcm_page,
    ListCreateAPIView_bes_page,
    DetailAPIview_bes_page,
    ListCreateAPIView_el_page,
    DetailAPIview_el_page,
    ListCreateAPIView_ma_page,
    DetailAPIview_ma_page
)

app_name = 'polyacetal'
router = routers.DefaultRouter()
urlpatterns = [
    path('index', ListCreateAPIView.as_view(), name='index_api'),  # 首頁get
    path('del/<str:pk>', DetailAPIview.as_view(),
         name='del-api'),  # 首頁get. post,
    path('ffmm', ListCreateAPIView_ffmm_page.as_view(), name='ffmm-api'),  # get
    path('ffmm/<str:pk>', DetailAPIview_ffmm_page.as_view(),
         name='ffmm-del-api'),  # get. post,
    path('bcm', ListCreateAPIView_bcm_page.as_view(), name='bcm-api'),  # get
    path('bcm/<str:pk>', DetailAPIview_bcm_page.as_view(),
         name='bcm-del-api'),  # get. post,
    path('bes', ListCreateAPIView_bes_page.as_view(), name='bes-api'),  # get
    path('bes/<str:pk>', DetailAPIview_bes_page.as_view(),
         name='bes-del-api'),  # get. post,
    path('el', ListCreateAPIView_el_page.as_view(), name='el-api'),  # get
    path('el/<str:pk>', DetailAPIview_el_page.as_view(),
         name='el-del-api'),  # get. post,
    path('ma', ListCreateAPIView_ma_page.as_view(), name='ma-api'),  # get
    path('ma/<str:pk>', DetailAPIview_ma_page.as_view(),
         name='ma-del-api'),  # get. post,

]

from django.urls import path, re_path
from . import views
from rest_framework import routers
from django.views.generic import TemplateView
from .views import (


    DetailAPIview,
    ListCreateAPIView
)

app_name = 'polyacetal'
router = routers.DefaultRouter()
urlpatterns = [
    path('index', ListCreateAPIView.as_view(), name='index_api'),
    path('ffmm', views.poly_home, name='ffmm-api'),
    path('del/<str:pk>', DetailAPIview.as_view(), name='del-api'),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

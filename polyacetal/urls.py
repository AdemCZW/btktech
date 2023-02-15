from django.urls import path
from . import views
from rest_framework import routers
from .views import (
    poly_index,
    apiviewset,
    DetailAPIview,
    ListCreateAPIView
)

app_name = 'polyacetal'
router = routers.DefaultRouter()
router.register('apiset', views.apiviewset)

urlpatterns = [
    path('api', views.poly_home, name='index-api'),
    path('api001', ListCreateAPIView.as_view(), name='list001'),
    path('del/<str:pk>', DetailAPIview.as_view(), name='del-api'),
]

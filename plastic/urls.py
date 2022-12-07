from django.urls import path
from .views import (
    PlatHome,
    PlatIndex
)

app_name = 'plastic'

urlpatterns = [
    path('', PlatHome.as_view(), name="home"),
    path('tw', PlatIndex.as_view(), name="index"),

]

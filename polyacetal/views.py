from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import home_poly, ffmm_page, bcm_page, bes_page, el_page, ma_page
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import poly_serializer, ffmm_serializer, bcm_serializer, bes_serializer, el_serializer, ma_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class ListCreateAPIView(generics.ListCreateAPIView):
    queryset = home_poly.objects.all()
    serializer_class = poly_serializer


class DetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = home_poly.objects.all()
    serializer_class = poly_serializer


class ListCreateAPIView_ffmm_page(generics.ListCreateAPIView):
    queryset = ffmm_page.objects.all()
    serializer_class = ffmm_serializer


class DetailAPIview_ffmm_page(generics.RetrieveUpdateDestroyAPIView):
    queryset = ffmm_page.objects.all()
    serializer_class = ffmm_serializer


class ListCreateAPIView_bcm_page(generics.ListCreateAPIView):
    queryset = bcm_page.objects.all()
    serializer_class = bcm_serializer


class DetailAPIview_bcm_page(generics.RetrieveUpdateDestroyAPIView):
    queryset = bcm_page.objects.all()
    serializer_class = bcm_serializer


class ListCreateAPIView_bes_page(generics.ListCreateAPIView):
    queryset = bes_page.objects.all()
    serializer_class = bes_serializer


class DetailAPIview_bes_page(generics.RetrieveUpdateDestroyAPIView):
    queryset = bes_page.objects.all()
    serializer_class = bes_serializer


class ListCreateAPIView_el_page(generics.ListCreateAPIView):
    queryset = el_page.objects.all()
    serializer_class = el_serializer


class DetailAPIview_el_page(generics.RetrieveUpdateDestroyAPIView):
    queryset = el_page.objects.all()
    serializer_class = el_serializer


class ListCreateAPIView_ma_page(generics.ListCreateAPIView):
    queryset = ma_page.objects.all()
    serializer_class = ma_serializer


class DetailAPIview_ma_page(generics.RetrieveUpdateDestroyAPIView):
    queryset = ma_page.objects.all()
    serializer_class = ma_serializer


@api_view(['GET'])
def poly_home(request):
    Apilists = home_poly.objects.all()
    serializer = poly_serializer(Apilists, many=True)
    return Response(serializer.data)

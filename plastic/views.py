from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import plat_home, plat_index
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class PlatHome(ListView):
    model = plat_home
    template_name = 'home_01.html'  # 樣板路徑


class PlatIndex(ListView):
    model = plat_index
    template_name = 'home_02.html'  # 樣板路徑

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import index_01, welding_01 ,welding_02, home, cpn_01 ,mta_01 ,sys_01 ,bc_01, qa_01, ca_01, food_01, automation_01, automotive_01, hygiene_01, medical_01, electronics_01, battery_01, consumer_01
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
def HomeListView(request):
    home_001 = home.objects.all()
    context = {
        'home_001': home_001
    }
    return render(request, 'nav.html', context)

class IndexListView(ListView):
    model = index_01
    template_name = 'home_01.html'  # 樣板路徑  

class Welding_01View(ListView):
    model = welding_01
    template_name = 'welding.html'  # 樣板路徑  

class Welding_02View(ListView):
    model = welding_02
    template_name = 'welding.html'  # 樣板路徑  

class cpn_01View(ListView):
    model = cpn_01
    template_name = 'components.html'  # 樣板路徑  

class mta_01View(ListView):
    model = mta_01
    template_name = 'metal.html'  # 樣板路徑  

class sys_01View(ListView):
    model = sys_01
    template_name = 'system.html'  # 樣板路徑  

class bc_01View(ListView):
    model = bc_01
    template_name = 'branches.html'  # 樣板路徑  

class qa_01View(ListView):
    model = qa_01
    template_name = 'qa.html'  # 樣板路徑  

class ca_01View(ListView):
    model = ca_01
    template_name = 'contact.html'  # 樣板路徑  

class food_01View(ListView):
    model = food_01
    template_name = 'food.html'  # 樣板路徑 

class automation_01View(ListView):
    model = automation_01
    template_name = 'automation.html'  # 樣板路徑 

class automotive_01View(ListView):
    model = automotive_01
    template_name = 'automotive.html'  # 樣板路徑

class hygiene_01View(ListView):
    model = hygiene_01
    template_name = 'hygiene.html'  # 樣板路徑 

class medical_01View(ListView):
    model = medical_01
    template_name = 'medical.html'  # 樣板路徑 

class electronics_01View(ListView):
    model = electronics_01
    template_name = 'electronics.html'  # 樣板路徑 

class battery_01View(ListView):
    model = battery_01
    template_name = 'battery.html'  # 樣板路徑 

class consumer_01View(ListView):
    model = consumer_01
    template_name = 'consumer.html'  # 樣板路徑 





from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, path
from django.views import generic

from .forms import *

def index(request):
    return render(request, "home.html")

# class BronPc(ListView):
#     model = Pc
#     template_name = 'hotel\hotel.html'


# class LoginUser(LoginView, DataMixin):
#     template_name = "login.html"
#     form_class = AuthenticationForm
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_user_context(title="Авторизация")
#         return dict(list(context.items()) + list(c_def.items()))

class SignUpView(generic.CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def Map(request):
    return render(request, "maps.html")

def bron(request):
    return render(request, "bron.html")

def info(request):
    return render(request, "info.html")
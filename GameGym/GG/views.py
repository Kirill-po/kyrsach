from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "home.html")

class BronPc(ListView):
    model = Pc
    template_name = 'hotel\hotel.html'

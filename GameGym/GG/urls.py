from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bron/', views.BronPc.as_view(), name='bron'),
]

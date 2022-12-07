from django.urls import path, include
from . import views
# from .views import LoginUser

urlpatterns = [
    path('', views.index, name='home'),
    # path('bron/', views.BronPc.as_view(), name='bron'),
    # path('login/', LoginUser.as_view(), name = 'login'),
    path('accounts/', include('django.contrib.auth.urls'), name = 'login'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
]

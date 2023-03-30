from django.urls import path
from .views import *

urlpatterns= [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name = 'logout'),
    path('profile/<str:slug>', profile, name='profile'),
    path('update/', update, name='update'),
    path('change/', reset, name='reset')
]
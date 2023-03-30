from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('post-detail/<str:postId>/<str:slug>',detail,  name='detail')
    
]
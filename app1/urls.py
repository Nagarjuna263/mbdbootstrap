from django.urls import path
from app1.views import *
app_name='nagarjuna'

urlpatterns = [
    path('mbd/',mbd,name='mbd'),
]

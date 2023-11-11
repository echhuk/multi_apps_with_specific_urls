from rcb.views import *
from django.urls import path

app_name='anything2'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('siraj',siraj,name='siraj'),

]
from mi.views import *
from django.urls import path

app_name='anything1'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('sky',sky,name='sky'),

]
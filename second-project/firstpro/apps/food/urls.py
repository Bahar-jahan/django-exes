
from django.urls import path 
from .views import *


urlpatterns = [
    path('', index , name='food_index'),
    path('pizza/', Pizza , name='Pizza'),
    path('order/', Order , name='Order'),
    path('humbugger/', Humbugger , name='Humbugger'),
    path('berengomorgh/', Sonati , name='Sonati'),
]

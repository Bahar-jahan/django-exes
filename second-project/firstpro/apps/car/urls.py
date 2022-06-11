from django.urls import path 
from .views import *


urlpatterns = [
    path('', index , name='car_index'),
    path('pride/', Pride , name='pride'),
    path('order/', Order , name='order'),
    path('lamborghini/', Lamborghini , name='lamborghini'),
]

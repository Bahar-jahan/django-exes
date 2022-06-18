
from django.urls import path 
from .views import *


urlpatterns = [
    path('', index , name='blog_index'),
    path('<int:id>/', PostView , name='blog_detail'),
   
]

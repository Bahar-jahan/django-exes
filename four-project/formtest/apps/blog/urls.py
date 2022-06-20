from django.urls import path
from .views import *
urlpatterns = [
    path('', index , name='blog_index'),
    path('<int:id>/', PostDetail , name='post_detail'),
    path('create/', CreatePost , name='post_create'),
]

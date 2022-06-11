from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    food_group = FoodGroup.objects.all()
    context = {
        'welcome': 'به رستوران ما خوش امدید',
        'food_group': food_group
    }
    return render(request, 'food/index.html', context)


def Pizza(request):
    foods = Food.objects.filter(food_group_id=2)
    context = {
        'welcome': 'به صفحه پیتزا خوش امدید',
        'foods': foods
    }
    return render(request, 'food/pizza.html', context)


def Order(request):
    context = {
        'welcome': 'به صفحه سفارش خوش امدید'
    }
    return render(request, 'food/order.html',context)


def Humbugger(request):
    foods = Food.objects.filter(food_group_id=3)
    context = {
        'welcome': 'به صفحه همبرگر خوش امدید',
        'foods': foods
    }
    return render(request, 'food/humbugger.html', context)


def Sonati(request):
    foods = Food.objects.filter(food_group_id=1)
    context = {
        'welcome': 'به صفحه برنج و مرغ خوش امدید',
        'foods': foods
    }
    return render(request, 'food/sonati.html', context)

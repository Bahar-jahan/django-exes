from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'welcome': 'به صفحه ماشین ها  خوش امدید',
        'carList': {
            'car1': 'lamborghini',
            'car2': 'Pride',
        },
        }
    return render(request,'car/index.html',context)


def Pride(request):
    context = {
        'welcome': 'به صفحه پراید خوش امدید',
        }
    return render(request,'car/pride.html',context)

def Lamborghini(request):
    context = {
        'welcome': 'به صفحه Lamborghini خوش امدید',
        }
    return render(request,'car/lamborgini.html',context)


def Order(request):
    context = {
        'welcome': 'به صفحه سفارش خوش امدید'
    }
    return render(request, 'car/order.html')

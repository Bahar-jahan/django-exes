from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'restaurant': 'خوشمزه طوری',
        'welcome': 'به رستوران ما خوش امدید',
        'menu': {
            'food1': 'پیتزا',
            'food2': 'همبرگر',
            'food3': 'برنج و مرغ',
        },
    }
    return render(request, 'food/index.html', context)


def Pizza(request):
    context = {

        'welcome': 'به صفحه پیتزا خوش امدید',
        'menu': {
            'food1': ' مرغ ',
            'food2': 'رست بیف',
            'food3': 'سبزیجات ',
            'food4': ' پپرونی ',
            'food5': ' مخصوص ',
            'food6': 'مارگاریتا  ',
            'food7': ' مخلوط ',
            'food8': ' خانواده ',
        },
    }
    return render(request, 'food/pizza.html', context)


def Order(request):
    context = {
        'welcome': 'به صفحه سفارش خوش امدید'
    }
    return render(request, 'food/order.html')


def Humbugger(request):
    context = {

        'welcome': 'به صفحه همبرگر خوش امدید',
        'menu': {
            'food1': ' چیز برگر ',
            'food2': 'قارچ برگر',
            'food3': 'دوبل ',
            'food4': ' دودی ',
            'food5': ' مخصوص ',
        },
    }
    return render(request, 'food/humbugger.html', context)


def Sonati(request):
    context = {

        'welcome': 'به صفحه برنج و مرغ خوش امدید',
        'menu': {
            'food1': 'برنج ومرغ سنتی  ',
            'food2': 'برنج ومرغ ترش',
            'food3': 'برنج ومرغ سرخ شده ',
            'food4': ' برنج ومرغ فسنجانی ',
        },
    }
    return render(request, 'food/sonati.html', context)

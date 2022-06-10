from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'welcome':'به وب سایت من خوش امدید ',
        'sections':{
            'sections1':'غذا',
            'sections2':'ماشین'
        }
               }
    return render(request ,'main/index.html' , context)
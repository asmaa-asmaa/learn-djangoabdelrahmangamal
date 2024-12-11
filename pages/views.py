from django.shortcuts import render
#from django.http import HttpResponse
from .models import Login
from .forms import LoginForm


# Create your views here.

def index(request):
    #return HttpResponse("hello world")
    #return render(request, 'pages/index.html',{'name': 'asmaa', 'age': 33})
    x= {'name': 'asmaa', 'age': 33}
    #x= {'name': '', 'age': 33}
    #x= {'name': 'asmaa ali mohsen ali', 'age': 33}
    #x= {'name': 'asmaa', 'age': 33}
    #x= {'name': 'asmaa mohamed ali', 'age': 33}
    #x= {'name': 'asmaa mohamed ali', 'age': 3333333333}


    



    return render(request, 'pages/index.html', x)


def about(request):
    #return HttpResponse('about page')

    # username= request.POST.get('username')
    # password=request.POST.get('password')
    # data= Login(username= username, password = password)
    # data.save()
    if request.method == 'POST':
    
      dataform =  LoginForm(request.POST)
      if dataform.is_valid():
         dataform.save()
    return render(request, 'pages/about.html',{'lf':LoginForm})


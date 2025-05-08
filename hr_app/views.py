from django.shortcuts import render

# Create your views here.
from hr_app.models import Data

from hr_app.models import Data
def index(request):
    data = Data.objects.all()
    context = {
        "data": data
    }
    return render(request,'index.html',context)
def table(request):
    data = Data.objects.all()
    context = {data
    }
    return render(request,'table.html',context)
def filter1(request):
    data = Data.objects.all()
    context = {
        "data": data
    }
    return render(request,'filter1.html',context)


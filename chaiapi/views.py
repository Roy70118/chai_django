from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
# Create your views here.


def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'all_chai.html', {'chais': chais})


def chai_detail(request, chai_id):
    chais = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chais': chais})


def home(request):
    return render(request, 'index.html')
#     return HttpResponse("<h1> Welcome to Chai's Django Project: Home page</h1>")


def about(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: About Page</h1>")


def contact(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Conatct page</h1>")

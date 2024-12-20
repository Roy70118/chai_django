from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'index.html')
#     return HttpResponse("<h1> Welcome to Chai's Django Project: Home page</h1>")


def about(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: About Page</h1>")


def contact(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Conatct page</h1>")

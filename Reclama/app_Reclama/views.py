from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def fun(request):
#    return HttpResponse("Вполне себе круто!")

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')
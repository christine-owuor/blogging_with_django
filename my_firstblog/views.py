from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lists(request):
    return render(request,'index.html')

def create(request):
    return HttpResponse("Hello Christine")

def details(request):
    pass

def update(request):
    pass

def delete(request):
    pass

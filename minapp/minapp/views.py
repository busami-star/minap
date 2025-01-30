# from django.http import HttpResponse
#
# def homepage(request):
#     return HttpResponse("Hello world")
#
# def about(request):
#     return HttpResponse("My about page")
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
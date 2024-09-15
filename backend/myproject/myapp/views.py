from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
# def example_view(request):
#     return JsonResponse({'message': 'Hello from Django!'})

def home(request):
    return HttpResponse("Welcome to the home page!")

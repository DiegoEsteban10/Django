from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Bienvenido a mi core app")
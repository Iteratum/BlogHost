from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "/index.html")

def BlogHost(request):
    return render(request, "/BlogHost.html")

def Contact(request):
    return render(request, "/Contact.html")

def Feature(request):
    return render(request, "/Feature.html")

def Pricing(request):
    return render(request, "/Pricing.html")
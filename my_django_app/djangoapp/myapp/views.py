from django.shortcuts import render

# Create your views here.
def beranda(request):
    return render(request, 'beranda.html')

def aboutus(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')
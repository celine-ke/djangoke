from django.shortcuts import render
def Nyumbani(request):
    return render(request, 'index.html')
def kuhusu(request):
    return render(request, 'about.html')
def kurasa(request):
    return render(request, 'donate.html')
def ingia(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
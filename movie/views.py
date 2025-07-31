from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Daza'})

def about(request):
    return render(request, 'about.html')

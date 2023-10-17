from django.shortcuts import render
import os


# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def register(request):
    return render(request, 'myapp/register.html')

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

def mylogin(request):
    return render(request, 'myapp/mylogin.html')

def profilemanagement(request):
    return render(request, 'myapp/profilemanagement.html')


def plot_view(request):
    plot_file_path = os.path.join('images', 'plot.png')
    return render(request, 'myapp/index.html', {'plot_file_path': plot_file_path})
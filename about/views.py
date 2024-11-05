from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'nama': 'Baltimore Ravens - Lamar Jackson ',
    }
    return render(request, 'index.html', context)
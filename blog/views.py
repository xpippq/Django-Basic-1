from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'name':'Blog Saya ',
    }
    return render (request, 'blog/blog.html', context)
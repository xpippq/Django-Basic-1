from django.shortcuts import render

# Create your views here.
def contact (request):
    context = {
        'name': 'Kontak saya',
    }
    return render(request, 'contact/contact.html', context)
from django.shortcuts import render
from . import views

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')


def about(request):
    return render(request, 'webpages/about.html')



def contact_us(request):
    return render(request, 'webpages/contact.html')

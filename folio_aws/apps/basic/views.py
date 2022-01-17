from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'basic/home_index.html')

def contact(request):
    return render(request, 'basic/contact_index.html')
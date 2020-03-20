from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests,'page/index.html')


def club(requests):
    return render(requests,'page/club.html')

def schedule(requests):
    return render(requests,'page/schedule.html')

def result(requests):
    return render(requests, 'page/result.html')

def blog(requests):
    return render(requests, 'page/blog.html')

def contact(requests):
    return render(requests, 'page/contact.html')

def details(requests):
    return render(requests, 'page/blog-details.html')
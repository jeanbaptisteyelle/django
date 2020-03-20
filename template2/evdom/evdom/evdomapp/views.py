from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, 'page/index.html')

def about(requests):
    return render(requests, 'page/about.html')

def service(requests):
    return render(requests, 'page/service.html')

def blog(requests):
    return render(requests, 'page/blog.html')

def single(requests):
    return render(requests, 'page/details-blog.html')

def rooms(requests):
    return render(requests, 'page/rooms.html')

def element(requests):
    return render(requests, 'page/element.html')

def contact(requests):
    return render(requests, 'page/contact.html')
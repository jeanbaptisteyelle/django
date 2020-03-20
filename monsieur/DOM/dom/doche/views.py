from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'page/index.html')

def about(requests):
    return render(requests, 'page/about.html')

def track(requests):
    return render(requests, 'page/track.html')

def blog(requests):
    return render(requests, 'page/blog.html')

def single(requests):
    return render(requests, 'page/blog-single.html')

def element(requests):
    return render(requests, 'page/element.html')

def contact(requests):
    return render(requests, 'page/contact.html')
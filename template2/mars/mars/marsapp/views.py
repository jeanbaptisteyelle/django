from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'page/index.html')

def courses(requests):
    return render(requests, 'page/courses.html')

def blog(requests):
    return render(requests, 'page/blog.html')

def single(requests):
    return render(requests, 'page/single-blog.html')

def event(requests):
    return render(requests, 'page/event.html')

def details(requests):
    return render(requests, 'page/event-details.html')

def admission(requests):
    return render(requests, 'page/admission.html')

def elements(requests):
    return render(requests, 'page/elements.html')

def contact(requests):
    return render(requests, 'page/contact.html')


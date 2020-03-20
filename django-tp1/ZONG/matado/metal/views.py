from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, 'page/index.html')

def about(requests):
    return render(requests, 'page/about.html')

def product(requests):
    return render(requests, 'page/product_list.html')

def single(requests):
    return render(requests, 'page/single-product.html')

def login(requests):
    return render(requests, 'page/login.html')

def ckeckout(requests):
    return render(requests, 'page/checkout.html')

def cart(requests):
    return render(requests, 'page/cart.html')

def confirmation(requests):
    return render(requests, 'page/confirmation.html')
def element(requests):
    return render(requests, 'page/element.html')

def blog(requests):
    return render(requests, 'page/blog.html')

def singleblog(requests):
    return render(requests, 'page/single-blog.html')

def contact(requests):
    return render(requests, 'page/contact.html')
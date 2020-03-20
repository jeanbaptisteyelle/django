"""matado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('product list', views.product, name='product'),
    path('single-product', views.single, name='single'),
    path('login', views.login, name='login'),
    path('checkout', views.ckeckout, name='checkout'),
    path('cart', views.cart, name='cart'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('element', views.element, name='element'),
    path('blog', views.blog, name='blog'),
    path('single-block', views.singleblog, name='single-block'),
    path('contact', views.contact, name='contact'),
]
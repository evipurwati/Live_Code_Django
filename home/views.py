from django.shortcuts import render
from .models import Barang

def home(request) :
    return render(request, 'home/home.html', {})

def home(request) :
    barangs = Barang.objects.all()
    return render(request, 'home/home.html', {'barangs': barangs})

# def blog_detail(request, blog_id) :
#     blogs = BlogPost.objects.get(pk=blog_id)
#     return render(request, 'Blog/blog_detail.html', {'blogs': blogs})
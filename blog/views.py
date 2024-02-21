from django.shortcuts import render
from .models import Blog


def get_blog_details(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog/blog-details.html', {'blog': blog})


from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})

@csrf_exempt
def addBlog(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        content = data['content']
        blog = Blog.objects.create(content=content)
        blog.save()
    return JsonResponse('Blog added', safe=False)

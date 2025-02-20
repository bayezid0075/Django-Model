from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.
def home (request):
    # fast method create a post 
    # Post(
    #     title="My First Post",
    #     content="This is my first post content.",
    #     published=True
    # ).save()

    # second method to create a new post
    # Post.objects.create(
    #     title="My fifth Post",
    #     content="This is my second post content.",
    #     published=True
    # )

    # Read all posts  
    posts = Post.objects.all()    
    return render(request,'posts.html', {'posts': posts})
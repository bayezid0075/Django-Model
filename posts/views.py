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
    # posts = Post.objects.all()
    # return render(request,'posts.html', {'posts': posts})

    # Lookup and filtering 
    #  posts = Post.objects.filter(id__in=[1,3])
    #  return render(request,'posts.html', {'posts': posts}) 

    # # update post 
    # post = Post.objects.get(id=2)
    # post.title = "My Updated Post"
    # post.save()
    posts = Post.objects.filter(published=True)
    print(posts)
    posts.update(published=False)
    return render(request,'posts.html', {'posts': posts})
from django.db import models

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return super().__str__()
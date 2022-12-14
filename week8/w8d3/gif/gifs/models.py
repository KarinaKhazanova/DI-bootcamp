from django.db import models


class Gif(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    url = models.URLField()
    uploader_name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    gifs =  models.ManyToManyField(Gif)
    
    def __str__(self):
        return f"{self.name}"
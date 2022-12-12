from django.db import models


# Create your models here.
class Family(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    
class Animal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    legs= models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey('Family', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Animal {self.name}"
    
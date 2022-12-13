from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField();
    email= models.TextField(unique=True);
    phone_number = PhoneNumberField()
    address = models.TextField()

    
    def __str__(self):
        return f"Person({self.id=}, {self.name=}, {self.phone_number=})"

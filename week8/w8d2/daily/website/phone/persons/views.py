from django.shortcuts import render
from persons.models import Person
from phonenumber_field.phonenumber import PhoneNumber

# Create your views here.


def phonenumber(request, phonenumber):
    context = {}
    person = Person.objects.filter(phone_number=phonenumber)
    context.update(person=person)
    return render(request, "phonenumber.html", context=context)


def name(request, name):
    context = {}
    person = Person.objects.filter(name=name)
    context.update(person=person)
    return render(request, "name.html", context=context)

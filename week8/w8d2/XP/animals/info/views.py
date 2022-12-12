import json

from django.shortcuts import render
from info.models import Animal, Family


# Create your views here.
def family(request, id):
    context = {}
    animals = Animal.objects.filter(family=id)

    context.update({"animals": animals})

    return render(
        request,
        "family.html",
        context=context,
    )


def animal(request, id):
    context = {}
    animal = Animal.objects.get(id=id)
    context.update({"animal": animal})
    return render(
        request,
        "animal.html",
        context=context,
    )


def animals(request):
    context = {"animals":Animal.objects.all()}
    return render(
        request,
        "animals.html",
        context=context,
    )

import json

from django.shortcuts import render

INFO_JSON = "info.json"

with open(INFO_JSON) as f:
    info_json = json.load(f)

# Create your views here.
def family(request, id):
    context = {}
    animals = info_json["animals"]
    animals_by_family = [animal for animal in animals if animal["family"] == id]
    context.update({"animals": animals_by_family})

    return render(
        request,
        "family.html",
        context=context,
    )


def animal(request, id):
    context = {}
    animals = info_json["animals"]
    animal_by_id = [animal for animal in animals if animal["id"] == id]
    context.update({"animal": animal_by_id})
    return render(request, "animal.html", context=context)

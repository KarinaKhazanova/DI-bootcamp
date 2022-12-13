from django.shortcuts import render

from people import data


# Create your views here.
def index(request):
    context = {}
    people_by_age = sorted(data.people, key=lambda human: human["age"])
    context.update(people=people_by_age)

    return render(request, "index.html", context=context)


def people(request, id):
    context = {}
    human = [human for human in data.people if human["id"] == id]
    context.update(human=human)
    return render(request, "people.html", context=context)

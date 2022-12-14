from django.shortcuts import redirect, render
from persons.forms import PhoneForm
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

def search_phone(request):
    context = {}
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phonenumber = form['phone'].value()
            return redirect('phonenumber', phonenumber=phonenumber)
    else:
        form = PhoneForm()
    context.update(form=form)
    return render(request, "search_phone.html", context=context)
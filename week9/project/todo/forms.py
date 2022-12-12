from django import forms
from .models import Category

class Category1(forms.Form):
    name = forms.CharField()
    image = forms.URLField()


class Todo1(forms.Form):
    title = forms
    details
    deadline_date
    category = forms.ModelChoiceField(queryset=Category1.objects.all())
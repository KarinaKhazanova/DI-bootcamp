from django import forms
from gifs.models import Category, Gif


class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = ['uploader_name', "title", "url"]
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
        
    def save(self):
        instance = forms.ModelForm.save(self)
        instance.category_set.clear()
        instance.category_set.add(*self.cleaned_data['categories'])
        return instance


class CategoryForm(forms.ModelForm):
     class Meta:
        model = Category
        fields = ['name']
        

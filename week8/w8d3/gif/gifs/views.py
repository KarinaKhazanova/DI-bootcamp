from django.shortcuts import redirect, render
from gifs.forms import CategoryForm, GifForm
from gifs.models import Category, Gif


# Create your views here.
def index(request):
    context = {}
    gifs = Gif.objects.all()
    context.update(gifs=gifs)
    return render(request, 'index.html', context=context)

def add_gif(request):
    context = {}
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            gif = form.save()
            return redirect('add_gif')
    else:
        form = GifForm()
    context.update(form=form)
    return render(request, 'add_gif.html', context=context,)

def add_category(request):
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()
    context.update(form=form)
    return render(request, 'add_category.html', context=context,)

def gif(request, gif_id):
    context = {}
    gif = Gif.objects.get(id=gif_id)
    context.update(gif=gif)
    return render(request, 'gif.html', context=context)

def category_gifs(request, category_id):
    context = {}
    category = Category.objects.get(id=category_id)
    gifs = category.gifs.all()
    context.update(gifs=gifs)
    return render(request, 'category_gifs.html', context=context)

def categories(request):
    context = {}
    categories = Category.objects.all()
    context.update(categories=categories)
    return render(request, 'categories.html', context=context)
from django.urls import path
from gifs import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('add-gif', views.add_gif, name="add_gif"),
    path('add-category', views.add_category, name="add_category"),
    path('categories', views.categories, name="categories"),
    path('category/<int:category_id>', views.category_gifs, name="category_gifs"),
    path('gif/<int:gif_id>', views.gif, name="gif"),
]

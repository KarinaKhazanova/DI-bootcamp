from django.urls import path
from persons import views

urlpatterns = [
    path("phonenumber/<phonenumber>", views.phonenumber, name="phonenumber"),
    path("name/<name>", views.name, name="name"),
]

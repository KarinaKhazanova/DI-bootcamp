from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField()


class Todo(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=30)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField()
    date_completion = models.DateField()
    deadline_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="todo")




# title
# details
# has_been_done : set by default to False
# date_creation (when the user created the todo)
# date_completion (when the user finished the todo)
# deadline_date (when the user has to finish the todo)
# category: One to Many relationship with the Category Model (ForeignKey)
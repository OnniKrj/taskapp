from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=100)
    task_date = models.DateField()
    
class TaskList(models.Model):
    title = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return reverse("list", args=[self.id])

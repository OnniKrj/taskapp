from django.db import models
from django.utils import timezone
from django.urls import reverse

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)
    
class TaskList(models.Model):
    task_name = models.CharField(max_length=50, unique=True)
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
      
    def __str__(self):
        return self.task_name
    
class Task(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )
    
    def __str__(self):
        return f"{self.task_name}: due {self.due_date}"
    
    class Meta:
        ordering = ["due_date"]
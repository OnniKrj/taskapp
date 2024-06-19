from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import TaskList, Task

class ListListView(ListView):
    model = TaskList
    template_name = "task_app/index.html"
    
class ItemListView(ListView):
    model = Task
    template_name = "task_app/task_list.html"
    
    def get_queryset(self):
        return Task.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    def get_context_data(self):
        context =  super().get_context_data()
        context["task_list"] = TaskList.objects.get(id=self.kwargs["list_id"])
        return context
from typing import Any
from django.urls import reverse
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView
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
    
class ListCreate(CreateView):
    model = TaskList
    fields = ["task_name"]
    
    def get_context_data(self):
        context =  super(ListCreate, self).get_context_data()
        context["task_name"] = "Add a new list"
        return context
    
class TaskCreate(CreateView):
    model = Task
    fields = [
        "todo_list",
        "task_name",
        "description",
        "due_date",
    ]
    
    def get_initial(self):
        initial_data = super(TaskCreate, self).get_initial()
        todo_list = TaskList.objects.get(id=self.kwargs["list_id"]) #  TARKISTA
        initial_data["todo_list"] = todo_list
        return initial_data
    
    def get_context_data(self):
        context = super(TaskCreate, self).get_context_data()
        todo_list = TaskList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["task_name"] = "Create a new item"
        return context
    
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id]) # TARKISTA

class TaskUpdate(UpdateView):
    model = Task
    fields = [
        "todo_list",
        "task_name",
        "description",
        "due_date",
    ]
    
    def get_context_data(self):
        context = super(TaskUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["task_name"] = "Edit item"
        return context
    
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])
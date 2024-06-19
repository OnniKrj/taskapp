from django.views.generic import ListView
from .models import TaskList

class ListListView(ListView):
    model = TaskList
    template_name = "task_app/index.html"
from django.contrib import admin
from task_app.models import Task, TaskList

admin.site.register(Task)
admin.site.register(TaskList)

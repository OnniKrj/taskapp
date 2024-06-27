# taskapp/task_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    # CRUD patterns for TaskLists
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    path("list/<int:pk>/delete/", views.TaskListDelete.as_view(), name="list-delete"),
    # CRUD patterns for Tasks
    path("list/<int:list_id>/item/add/", views.TaskCreate.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/", views.TaskUpdate.as_view(), name="item-update"),
    path("list/<int:list_id>/item/<int:pk>/delete/", views.TaskDelete.as_view(), name="item-delete",),
]

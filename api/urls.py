from django.urls import path
from .views import TodoListView, TodoDetailView, ApiOverview

urlpatterns = [
    path('', ApiOverview.as_view(), name='api-overview'),
     # URL for listing all Todo and creating a new Todo
    path('tasks/', TodoListView.as_view(), name='todo-list'),
    # URL for retrieving, updating, or deleting a specific Todo
    path('tasks/<int:pk>/',TodoDetailView.as_view(), name='todo-detail'),
]
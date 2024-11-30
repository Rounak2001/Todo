from .models import ToDoTask
from .serializers import ToDoTaskSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

class TodoListView(generics.ListCreateAPIView):
    """
    Handles GET (list all notes) and POST (create a new note) requests
    Replaces getNotes and createNote function-based views
    """
    queryset = ToDoTask.objects.all().order_by('-updated_at')
    serializer_class = ToDoTaskSerializer
    def perform_create(self, serializer):
        serializer.save()

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (retrieve), PUT (update), and DELETE requests for a specific note
    Replaces getNote, updateNote, and deleteNote function-based views
    """
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer
    lookup_field = 'pk' 


class ApiOverview(APIView):
    """
    Class-based view to provide an overview of API endpoints.
    """

    def get(self, request, *args, **kwargs):
        routes = [
            {
                'Endpoint': '/tasks/',
                'method': 'GET',
                'body': None,
                'description': 'Returns a list of all tasks'
            },
            {
                'Endpoint': '/tasks/',
                'method': 'POST',
                'body': {'title': 'string', 'description': 'string', 'is_completed': 'boolean'},
                'description': 'Creates a new task'
            },
            {
                'Endpoint': '/tasks/<id>/',
                'method': 'GET',
                'body': None,
                'description': 'Returns a specific task by ID'
            },
            {
                'Endpoint': '/tasks/<id>/',
                'method': 'PUT',
                'body': {'title': 'string', 'description': 'string', 'is_completed': 'boolean'},
                'description': 'Updates an existing task'
            },
            {
                'Endpoint': '/tasks/<id>/',
                'method': 'DELETE',
                'body': None,
                'description': 'Deletes a specific task by ID'
            },
            
        ]
        return Response(routes)

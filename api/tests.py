from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import ToDoTask

class ToDoTaskAPITests(APITestCase):

    def setUp(self):
        # Create sample tasks for testing
        self.task1 = ToDoTask.objects.create(title="Task 1", description="Description 1", is_completed=False)
        self.task2 = ToDoTask.objects.create(title="Task 2", description="Description 2", is_completed=True)
        
        # URL for the list of tasks
        self.list_url = reverse('todo-list')  # Ensure this matches your URL pattern name for the list view

    # Test listing all tasks
    def test_list_tasks(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Test creating a task
    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'New Task Description', 'is_completed': False}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToDoTask.objects.count(), 3)  # 2 from setup + 1 new
        self.assertEqual(response.data['title'], 'New Task')
        self.assertEqual(response.data['description'], 'New Task Description')
        

    # Test retrieving a specific task
    def test_retrieve_task(self):
        retrieve_url = reverse('todo-detail', args=[self.task1.id])  # Ensure this matches your URL pattern name for the detail view
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task1.title)

    # Test updating a specific task
    def test_update_task(self):
        update_url = reverse('todo-detail', args=[self.task1.id])  # Ensure this matches your URL pattern name for the detail view
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'is_completed': True}
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()  # Refresh object from database
        self.assertEqual(self.task1.title, 'Updated Task')
        self.assertTrue(self.task1.is_completed)

    # Test deleting a specific task
    def test_delete_task(self):
        delete_url = reverse('todo-detail', args=[self.task1.id])  # Ensure this matches your URL pattern name for the detail view
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ToDoTask.objects.count(), 1)  # One task should remain

    def test_delete_all_tasks(self):
        # Make a DELETE request to the endpoint
        response = self.client.delete('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDoTask.objects.count(), 0)
        self.assertIn("Deleted 2 tasks successfully.", response.data["message"])

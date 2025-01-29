from django.test import TestCase
from django.utils.timezone import now, timedelta
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Task
from django.urls import reverse

class TaskViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            'title': 'Task ViewSet',
            'description': 'Test ViewSet',
            'due_date': now() + timedelta(days=1),
            'completed': False
        }
        self.task = Task.objects.create(**self.task_data)

    def test_get_tasks(self):
        url = reverse('task-list')  # URL for the list view
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], self.task.title)

    def test_create_task(self):
        url = reverse('task-list')
        task_data = {
            'title': 'New Task',
            'description': 'New Task Description',
            'due_date': now() + timedelta(days=2),
            'completed': False
        }
        response = self.client.post(url, task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.last().title, task_data['title'])

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        updated_data = {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'due_date': now() + timedelta(days=3),
            'completed': True
        }
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data['title'])
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

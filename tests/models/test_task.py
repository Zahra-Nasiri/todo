from django.test import TestCase
from django.utils.timezone import now, timedelta

from tasks.models import Task


class TaskModelTestCase(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date=now() + timedelta(days=1),
            completed=False,
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertFalse(task.completed)
        self.assertEqual(str(task), 'Test Task')

    def test_due_date_validation(self):
        with self.assertRaises(Exception) as context:
            Task.objects.create(
                title='Invalid Task',
                description='Due date in the past',
                due_date=now() - timedelta(days=1),
            )
        self.assertIn(
            'Due date cannot be before the created date',
            str(context.exception),
        )

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        created_at = self.created_at or now()
        if self.due_date < created_at:
            raise ValidationError(
                'Due date cannot be before the created date.')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

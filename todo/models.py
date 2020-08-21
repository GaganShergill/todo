from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class ToDo(models.Model):
    task = models.CharField(max_length=256)
    date_created = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def complete(self):
        self.completed = True
        self.save()

    def notComplete(self):
        self.completed = False
        self.save()

    def get_absolute_url(self):
        return reverse('todo:taskList')

    def __str__(self):
        return self.task

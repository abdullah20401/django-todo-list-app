from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    task_name = models.CharField(max_length=254)
    task_complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "%s - %s" % (self.task_name, self.task_complete)
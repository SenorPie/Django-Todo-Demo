from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=60)
    done = models.BooleanField("Task done", default=False)
    date_created = models.DateTimeField("Date added", auto_now_add=True)

    def __str__(self):
        return self.task

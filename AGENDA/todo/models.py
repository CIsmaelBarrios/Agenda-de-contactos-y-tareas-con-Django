from django.db import models
from datetime import date

class Todo(models.Model):
    tittle=models.CharField(max_length=100, null=False, blank=False)
    description=models.TextField(max_length=100, blank=True, null=True)
    date=models.DateField(default=date.today)
    estimated_end=models.DateField(blank=True, null=True)
    priority=models.IntegerField(default=3)

    def __str__(self):
        return self.tittle
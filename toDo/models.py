from django.db import models
from django.conf import settings

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

class ToDo(models.Model):
    PRIORITY = (
        ("PRI", "Primary"),
        ("SEC", "Secondary"),
    )
    title = models.CharField(max_length=30)
    priority = models.CharField(max_length=3, choices=PRIORITY)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

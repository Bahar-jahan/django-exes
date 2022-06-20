from django.db import models
from  django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = [('drf', 'Draft'), ('pub', 'Published')]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
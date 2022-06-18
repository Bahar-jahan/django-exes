from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)

    def __str__(self):
        return self.name+' ' + self.family


class Post(models.Model):
    STATUS_CHOICES = [('drf', 'Draft'), ('pub', 'Published')]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

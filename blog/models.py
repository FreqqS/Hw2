from django.db import models


class Blog(models.Model):
    title = models.CharField(null=False, max_length=150, default='')
    text = models.TextField(null=False)
    author = models.CharField(null=False, max_length=120)

    def __str__(self):
        return f'ID {self.id} {self.title}'
from django.db import models


class Movie(models.Model):
    title = models.CharField(null=False, max_length=150, default='')
    description = models.TextField(null=False)
    producer = models.CharField(null=False, max_length=120)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return f'ID {self.id} {self.title}'
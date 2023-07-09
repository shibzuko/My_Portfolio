from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()

    def __str__(self):  # Позволяет показывать названия проектов в админке
        return self.title  # можно также добавить описание

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # blank=True - позволяет открывать ссылку в новой вкладке

    def __str__(self):  # Позволяет показывать названия проектов в админке
        return self.title  # можно также добавить описание


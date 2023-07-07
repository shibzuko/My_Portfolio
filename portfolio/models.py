from django.db import models

class Project(models.Model):
    id = models.AutoField(),
    title = models.CharField(max_length=100),
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # blank=True - позволяет открывать ссылку в новой вкладке


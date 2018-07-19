from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')  # Django wie, że folder 'images' będzie w folderze 'media'
    summary = models.CharField(max_length=200)

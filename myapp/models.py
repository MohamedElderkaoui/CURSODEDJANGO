from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=100)
    
class task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    description = models.TextField()
    
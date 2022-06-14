from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    link = models.URLField(max_length=250)
    project_image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name


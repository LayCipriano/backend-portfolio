from django.db import models

# Create your models here.

class Projetos(models.Model):
  title = models.CharField(max_length=200) 
  description = models.TextField()
  linkProject = models.CharField(max_length=200, blank=True)
  linkRepo = models.CharField(max_length=200)
  image = models.ImageField(upload_to='imagens/')
  
  def __str__(self):
    return f"{self.image} - {self.title} - {self.description} - {self.linkProject} - {self.linkRepo}"

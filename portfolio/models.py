from django.db import models

# Create your models here.


#------BLOG--------
class Blog(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField(max_length=50)
    area = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='areas'
    )
    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    areas = models.ManyToManyField(
        Area,
        related_name='autores'
    )
    def __str__(self):
        return self.nome

#------COURSES---------------




#-------PROJECTS--------------


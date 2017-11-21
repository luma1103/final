from django.db import models
from django.utils import timezone

# TAbla materia en la cual seran agregadas las nuevas materias
class Materia(models.Model):
    # campos 
    nombre = models.CharField(max_length=200)
    catedratico = models.CharField(max_length=200)
    # una breve descripcion de la materia
    text = models.TextField()
    


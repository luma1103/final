from django.db import models
from django.utils import timezone

# TAbla materia en la cual seran agregadas las nuevas materias
class Materia(models.Model):
    # Debe llevar campo nombre
    Nombre = models.CharField(max_length=200)
    # una breve descripcion de la materia
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

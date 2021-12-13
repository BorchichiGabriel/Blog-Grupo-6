from django.db import models
"""Esta clase es de prueba y es modificable fue creada con el fin de aplicar
las configuraciones del .gitignore"""
class Blogs(models.Model):
    titulo= models.CharField(max_length=255)
    contenido=models.CharField(max_length=255)

    def __str__(self) :
        return self.titulo


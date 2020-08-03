from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Doctor(models.Model):
    """!
    Clase que contiene los doctores
    """

    ## Nombre
    first_name = models.CharField('nombres', max_length=100)

    ## Apellido
    last_name = models.CharField('apellidos', max_length=100)

    ## Número telefónico
    phone = models.CharField(
        'teléfono',
        max_length=15,
    )

    ## Correo electrónico
    email = models.CharField(
        'correo electrónico', max_length=100, help_text=('correo@correo.com')
    )

    ## Dirección
    address = models.CharField('dirección', max_length=100)



    def __str__(self):
        return '%s %s, %s' % (self.first_name, self.last_name)



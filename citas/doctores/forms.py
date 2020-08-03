from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Doctor


class DoctorForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario
    """

    ## Nombre
    first_name = forms.CharField(
        label=_('Nombres:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Nombres de la Persona'),
            }
        )
    )

    ## Apellido
    last_name = forms.CharField(
        label=_('Apellidos:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Apellidos de la Persona'),
            }
        )
    )

    ## Número telefónico
    phone = forms.CharField(
        label=_('Teléfono:'),
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'placeholder': '+58-000-0000000',
                'data-toggle': 'tooltip', 'data-mask': '+00-000-0000000',
                'title': _('Indique el número telefónico de contacto'),
            }
        ),
        help_text=_('(país)-área-número')
    )

    ## Correo Electrónico
    email = forms.EmailField(
        label=_('Correo Electrónico:'),
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip',
                'title': _('Indique el correo electrónico de contacto con el usuario')
            }
        )
    )

    ## Dirección
    address = forms.CharField(
        label=_('Dirección:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'data-toggle': 'tooltip',
                'title': _('Indique la dirección exacta'),
            }
        )
    )

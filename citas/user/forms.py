from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class ProfileForm(forms.ModelForm):
   
    username = forms.CharField(
        label=_('Nombre de Usuario:'), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique el nombre de usuario'),
            }
        )
    )

    first_name = forms.CharField(
        label=_('Nombres:'), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Nombres'),
            }
        )
    )

    last_name = forms.CharField(
        label=_('Apellidos:'), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Apellidos'),
            }
        )
    )

    email = forms.EmailField(
        label=_('Correo Electrónico:'), max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'data-toggle': 'tooltip',
                'title': _('Indique el correo electrónico')
            }
        )
    )

    phone = forms.CharField(
        label=_('Teléfono:'), max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'placeholder': '+58-000-0000000',
                'data-mask': '+00-000-0000000',
                'title': _('Indique el número telefónico')
            }
        )
    )

    password = forms.CharField(
        label=_('Contraseña:'), max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique una contraseña de aceso al sistema')
            }
        )
    )

    confirm_password = forms.CharField(
        label=_('Confirmar Contraseña:'), max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique nuevamente la contraseña de aceso al sistema')
            }
        )
    )

    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError(_('El correo ya esta registrado'))
        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError(_('La contraseña no es la misma'))

        return confirm_password

    class Meta:

        model = User
        exclude = ['profile','date_joined']

class ProfileUpdateForm(ProfileForm):

    def __init__(self, *args, **kwargs):

        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirm_password'].required = False
        self.fields['password'].widget.attrs['disabled'] = True
        self.fields['confirm_password'].widget.attrs['disabled'] = True

    def clean_email(self):

        email = self.cleaned_data['email']
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(_('El correo ya esta registrado'))
        return email

    class Meta:
        
        model = User
        exclude = [
            'profile','password','confirm_password','date_joined','last_login','is_active','is_superuser','is_staff'
        ]

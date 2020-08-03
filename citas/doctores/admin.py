from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Person al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-07-2018
    """

    ## Mostrar los campos de la clase
    list_display = ['first_name','last_name','phone']

    ## Seleccionar campo para ordenar
    ordering = ['first_name']

admin.site.register(Doctor, DoctorAdmin)

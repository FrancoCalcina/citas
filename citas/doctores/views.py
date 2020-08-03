from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Doctor
from .forms import DoctorForm

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class DoctorListView(ListView):
    """!
    Clase que muestra la lista de doctores
    """

    model = Doctor
    template_name = 'Doctor/list.html'

    def get_queryset(self):
        """!
        Función que obtiene la lista de personas que están asociados al usuario

        """

        queryset = Doctor.objects.filter(user=self.request.user)
        return queryset

class DoctorCreateView(SuccessMessageMixin, CreateView):
    """!
    Clase que permite a un usuario registrar Doctores
    """
    model = Doctor
    form_class = DoctorForm
    template_name = 'Doctor/create.html'
    success_url = reverse_lazy('Doctor:list')
    def form_valid(self, form):
        """!
        Función que valida si el formulario está correcto

        @author William Páez (paez.william8 at gmail.com)
        @date 06-07-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario
        @return super <b>{object}</b> Formulario validado
        """

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(DoctorCreateView, self).form_valid(form)

class DoctorUpdateView(SuccessMessageMixin, UpdateView):
    """!
    Clase que permite a un usuario actualizar los datos de un doctor

    """

    model = Doctor
    form_class = DoctorForm
    template_name = 'Doctor/create.html'
    success_url = reverse_lazy('Doctor:list')

    def dispatch(self, request, *args, **kwargs):
        """!
        Función que valida si el usuario del sistema tiene permisos para entrar a esta vista

        @author William Páez (wpaez at cenditel.gob.ve)
        @date 06-07-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene los datos de la petición
        @param *args <b>{tuple}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return super <b>{object}</b> Entra a la vista de actualización de una persona,
            sino redirecciona hacia la vista de error de permisos
        """

        if Doctor.objects.filter(pk=self.kwargs['pk'],user=self.request.user):
            return super(DoctorUpdateView, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        """!
        Función que agrega valores predeterminados a los campos del formulario

        @author William Páez (paez.william8 at gmail.com)
        @date 06-07-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return initial_data <b>{object}</b> Valores predeterminado de los campos del formulario
        """

        initial_data = super(DoctorUpdateView, self).get_initial()
        return initial_data

class DoctorDeleteView(SuccessMessageMixin, DeleteView):
    """!
    Clase que permite a un usuario eliminar los datos

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-07-2018
    """

    model = Doctor
    template_name = 'Doctor/delete.html'
    success_url = reverse_lazy('Doctor:list')

    def dispatch(self, request, *args, **kwargs):
        """!
        Función que valida si el usuario del sistema tiene permisos para entrar a esta vista

        """

        if Doctor.objects.filter(pk=self.kwargs['pk'],user=self.request.user):
            return super(DoctorDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """!
        Función que retorna el mensaje de confirmación de la eliminación
        """

        messages.success(self.request, self.success_message)
        return super(DoctorDeleteView, self).delete(request, *args, **kwargs)

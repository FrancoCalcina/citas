from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from .forms import ProfileForm, ProfileUpdateForm
from .models import Profile
from base.constant import CREATE_MESSAGE, UPDATE_MESSAGE
from django.contrib.messages.views import SuccessMessageMixin


class ProfileCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = ProfileForm
    template_name = 'user/profile.create.html'
    success_url = reverse_lazy('user:login')
    success_message = CREATE_MESSAGE

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.set_password(form.cleaned_data['password'])
        self.object.is_active = True
        self.object.save()

        profile = Profile.objects.create(
            phone = form.cleaned_data['phone'],
            user= self.object
        )

        return super(ProfileCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ProfileCreateView, self).form_invalid(form)

class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'user/profile.create.html'
    success_url = reverse_lazy('base:home')
    success_message = UPDATE_MESSAGE

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.id == self.kwargs['pk'] and Profile.objects.filter(user=self.request.user):
            return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_initial(self):

        initial_data = super(ProfileUpdateView, self).get_initial()
        initial_data['phone'] = self.object.profile.phone
        return initial_data

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.save()

        if Profile.objects.filter(user=self.object):
            profile = Profile.objects.get(user=self.object)
            profile.phone = form.cleaned_data['phone']
            profile.save()

        return super(ProfileUpdateView, self).form_valid(form)

class ProfileDetailView(DetailView):
    model = User
    template_name = 'user/profile.detail.html'

    def dispatch(self, request, *args, **kwargs):
        """!
        Función que valida si el usuario del sistema tiene permisos para entrar a esta vista
        """

        if self.request.user.id == self.kwargs['pk'] and Profile.objects.filter(user=self.request.user):
            return super(ProfileDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

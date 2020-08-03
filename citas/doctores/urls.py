from django.urls import path
from .views import DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView
from django.contrib.auth.decorators import login_required

app_name = 'doctores'

urlpatterns = [
    path('list/', login_required(DoctorListView.as_view()), name='list'),
    path('create/', login_required(DoctorCreateView.as_view()), name='create'),
    path('update/<int:pk>/', login_required(DoctorUpdateView.as_view()), name='update'),
    path('delete/<int:pk>/', login_required(DoctorDeleteView.as_view()), name='delete'),
]

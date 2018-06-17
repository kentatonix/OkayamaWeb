from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import PersonalData


class SignUpCreateView(CreateView):
    model = PersonalData
    fields = ["name", "email", "password"]
    success_url = reverse_lazy('MachineEcWeb:index')



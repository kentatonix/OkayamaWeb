from django.urls import path
from MachineEcWeb.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
]
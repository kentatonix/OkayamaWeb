from django.urls import path
from accounts.views import SignUpCreateView

urlpatterns = [
    path('', SignUpCreateView.as_view(), name="create"),
]


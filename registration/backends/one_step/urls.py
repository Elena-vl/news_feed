"""
URLconf for registration using django-registration's one-step
workflow.

"""

from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views
from django.urls import path

urlpatterns = [
    path('register/',
        views.RegistrationView.as_view(),
        name='django_registration_register'),
    path('register/closed/',
        TemplateView.as_view(
            template_name='registration/registration_closed.html'
        ),
        name='django_registration_disallowed'),
    path('register/complete/',
        TemplateView.as_view(
            template_name='registration/registration_complete.html'
        ),
        name='django_registration_complete'),
]

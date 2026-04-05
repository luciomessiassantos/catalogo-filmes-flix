from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage, name='home'),
    path('filme/<int:id>/', Details, name="filme_detalhe")
]

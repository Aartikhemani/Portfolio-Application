from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('savecontact/', contactView, name='savecontact'),

]
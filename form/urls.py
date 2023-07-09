from django.urls import path
from .views import *


urlpatterns = [
    path('login/', Auth.as_view(), name= 'login'),
    path('traitym/', Heart.as_view(), name='TraiTym')
]

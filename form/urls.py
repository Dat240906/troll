from django.urls import path
from .views import *


urlpatterns = [
    path('login/', Auth.as_view(), name= 'login'),
    path('product/', Product.as_view(), name='product')
]

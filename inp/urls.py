from django.urls import path
from .views import index, output

urlpatterns = [
    path('', index, name='Main'),
    path('output/', output, name='Output'),
]

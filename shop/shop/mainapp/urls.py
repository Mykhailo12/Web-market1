from django.urls import path
from mainapp.views import test_view

urlpatterns = [
    path('', test_view, name='base'),
]

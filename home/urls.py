from django.urls import path
from .views import index_home_view

urlpatterns = [
    path('', index_home_view, name='index_home'),
]
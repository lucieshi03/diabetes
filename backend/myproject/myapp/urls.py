from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Default route
    # path('example/', views.example_view, name='example_view'),
]

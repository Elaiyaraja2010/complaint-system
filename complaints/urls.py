from django.urls import path
from . import views

urlpatterns = [
    path('', views.raise_complaint,name='raise_complaint'),
    path('status/', views.check_status, name='status'),
]

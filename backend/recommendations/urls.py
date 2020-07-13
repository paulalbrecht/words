from django.urls import path

from . import views

urlpatterns = [
    path('count/<int:count>/', views.by_count, name='by_count'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('uy/', views.SalomApiView.as_view()),
    path('uy/<int:pk>/', views.SalomDetailApiView.as_view()),
]
from django.urls import path
from app.views import obtener_efemerides  # Ajusta según la ubicación real de tu vista

urlpatterns = [
    path('calendario/', obtener_efemerides, name='obtener_efemerides'),
    # ... otras rutas ...
]

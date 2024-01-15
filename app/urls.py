from django.contrib import admin
from django.urls import include, path
from app.views import obtener_efemerides

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Incluye las rutas de tu aplicación 'app'
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('calendario/', obtener_efemerides, name='obtener_efemerides'),
]

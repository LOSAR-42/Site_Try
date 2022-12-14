from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# обращение идет в *приложение*.urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contact', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import dashboard
from inventory import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # The root URL '/' is handled by the dashboard view
    path('', views.dashboard, name='dashboard'),
    # All inventory-related URLs are included under /inventory/
    # AND are given the namespace 'inventory'
    path('inventory/', include('inventory.urls', namespace='inventory')),
    # Add accounts URLs with namespace
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # Add sales URLs with namespace
    path('sales/', include('sales.urls', namespace='sales')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



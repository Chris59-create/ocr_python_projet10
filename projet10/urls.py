from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('app_authentication.urls',
                         namespace='app_authentication')),
    path('api/', include('app_softdesk.urls', namespace='app_softdesk')),
]

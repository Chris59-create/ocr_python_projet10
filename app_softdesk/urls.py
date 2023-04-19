from django.urls import path, include
from rest_framework import routers

from .views import ProjectViewset

app_name = 'app_softdesk'

router = routers.SimpleRouter()
router.register('project', ProjectViewset, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]

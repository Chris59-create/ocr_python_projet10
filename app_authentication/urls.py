from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import SignupAPIView, ContributorViewset

app_name = 'app_authentication'

router = routers.SimpleRouter()
router.register('contributor', ContributorViewset, basename='project')

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, PlacementDriveViewSet, ApplicationViewSet,
    MockTestViewSet, MockTestResultViewSet
)

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'drives', PlacementDriveViewSet)
router.register(r'applications', ApplicationViewSet, basename='application')
router.register(r'mock-tests', MockTestViewSet)
router.register(r'mock-test-results', MockTestResultViewSet, basename='mock-test-result')

urlpatterns = [
    path('', include(router.urls)),
]

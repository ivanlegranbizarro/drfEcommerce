from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, CategoryViewSet

router = DefaultRouter()

router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"brands", BrandViewSet, basename="brand")

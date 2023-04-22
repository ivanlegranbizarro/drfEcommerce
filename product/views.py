from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


@extend_schema(tags=["categories"])
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(tags=["brands"])
class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving brands.
    """
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(tags=["products"])
class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving products.
    """
    queryset = Product.objects.all().filter(is_active=True).prefetch_related(
        "brand", "category").select_related("brand", "category")

    lookup_field = "slug"

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(
            slug=slug).select_related("brand", "category").first())
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    @action(detail=False, methods=["get"], url_path=r"category/(?P<category>[\w-]+)", url_name="list_products_by_category")
    def list_products_by_category(self, request, category=None):
        """
        List all products by category
        """
        queryset = self.queryset.filter(category__slug=category).select_related(
            "brand", "category")
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

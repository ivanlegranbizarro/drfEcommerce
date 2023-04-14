from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


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

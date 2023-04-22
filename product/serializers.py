from rest_framework import serializers

from .models import Brand, Category, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductLineSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ProductLine
        exclude = ('id', 'product', 'is_active')


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    category_name = serializers.CharField(
        source='category.name', read_only=True)
    product_lines = ProductLineSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'description', 'is_digital',
                  'brand_name', 'category_name', 'product_lines')

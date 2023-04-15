import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    url = reverse("category-list")

    def test_category_get(self, category_factory, api_client):
        category = category_factory()
        response = api_client.get(self.url)
        assert response.status_code == 200
        assert len(response.data) > 0
        assert response.data[0]["name"] == str(category.name)
        assert response.headers["Content-Type"] == "application/json"


class TestBrandEndpoints:
    url = reverse("brand-list")

    def test_brand_get(self, brand_factory, api_client):
        brand = brand_factory()
        response = api_client.get(self.url)
        assert response.status_code == 200
        assert len(response.data) > 0
        assert response.data[0]["name"] == str(brand.name)
        assert response.headers["Content-Type"] == "application/json"


class TestProductEndpoints:
    url = reverse("product-list")

    def test_product_get(self, product_factory, api_client):
        product = product_factory()
        response = api_client.get(self.url)
        assert response.status_code == 200
        assert len(response.data) > 0
        assert response.data[0]["name"] == str(product.name)
        assert response.data[0]["brand"] == product.brand.id
        assert response.data[0]["category"] == product.category.id
        assert response.data[0]["description"] == str(product.description)
        assert response.data[0]["is_digital"] == product.is_digital
        assert response.headers["Content-Type"] == "application/json"

import factory
from factory.faker import Faker

from product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = Faker("word")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = Faker("word")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker("word")
    description = Faker("text")
    is_digital = Faker("boolean")
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)

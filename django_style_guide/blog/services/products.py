from django.db.models import QuerySet
from django_style_guide.blog.models import Product

def create_product(name: str) -> QuerySet[Product]:
    return Product.objects.create(name=name)




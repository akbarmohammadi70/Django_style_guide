from django.db.models import QuerySet
from django_style_guide.blog.models import Product

def get_products() -> QuerySet[Product]:
    return Product.objects.all()




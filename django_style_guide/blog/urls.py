from django.urls import path, include
from django_style_guide.blog.apis.products import ProductApi
urlpatterns = [
     path('product/', ProductApi.as_view(),name="product")
]

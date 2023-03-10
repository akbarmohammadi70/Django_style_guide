from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django_style_guide.api.pagination import LimitOffsetPagination
from django_style_guide.blog.models import Product

from django_style_guide.blog.services.products import create_product
from django_style_guide.blog.selectors.products import get_products
from drf_spectacular.utils import extend_schema


class ProductApi(APIView):

    class Pagination(LimitOffsetPagination):
        default_limit = 15

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)

    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ("name", "created_at", "updated_at")

    @extend_schema(request=InputSerializer, responses=OutPutSerializer)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_product(name=serializer.validated_data.get("name"))
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(self.OutPutSerializer(query, context={"request":request}).data)

    @extend_schema(responses=OutPutSerializer)
    def get(self, request):
        query = get_products()
        return Response(self.OutPutSerializer(query, context={"request":request}, many=True).data)
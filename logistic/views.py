from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination


class ProductViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['title', 'description']
    pagination_class = PageNumberPagination


class StockViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_fields = ['products']
    pagination_class = PageNumberPagination

from rest_framework import filters
from rest_framework import generics
from .models import Book
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend




class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['price','title','stock']
    filterset_fields = ['category','author']
    search_fields = ['author__name','category__name']

class BookDetailAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookDetailSerializer
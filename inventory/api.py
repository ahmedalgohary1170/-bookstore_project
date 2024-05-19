from rest_framework import generics
from .models import Book
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend




class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price','stock','author']

class BookDetailAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookDetailSerializer
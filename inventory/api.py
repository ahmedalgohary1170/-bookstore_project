from rest_framework import generics
from .models import Book
from . import serializers



class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookListSerializer


class BookDetailAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookDetailSerializer
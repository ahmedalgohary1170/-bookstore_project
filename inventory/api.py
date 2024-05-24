from rest_framework import filters
from rest_framework import generics
from .models import Book
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets




class CreateUpdateDetailDelete(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer   
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['price','title','stock']
    filterset_fields = ['category','author']
    search_fields = ['author__name','category__name']







# class BookListAPI(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = serializers.BookSerializer
#     filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
#     ordering_fields = ['price','title','stock']
#     filterset_fields = ['category','author']
#     search_fields = ['author__name','category__name']

# class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = serializers.BookSerializer
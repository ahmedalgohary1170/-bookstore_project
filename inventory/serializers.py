from rest_framework import serializers
from .models import Book



class BookListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

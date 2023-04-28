from rest_framework import serializers
from .models import Book, BookReview

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('book_id','title','author')

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookReview
        fields='__all__'
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, Http404
from .data import books
from .serializers import BookSerializer

# Create your views here.

class BookList(View):
    def get(self, request):
        serialized_books=BookSerializer(books, many=True).data
        return JsonResponse(serialized_books, safe=False)

class BookDetail(View):
    def get(self, request, book_id):
        bookFound=None
        for book in books:
            if book["book_id"]==book_id:
                bookFound=book
                break
        if bookFound:
            return JsonResponse(BookSerializer(bookFound).data, safe=False)
        else:
            raise Http404("Book not found")
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from .data import books
from .serializers import BookSerializer, BookReviewSerializer
import json

# Create your views here.

book_reviews=[]

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
        

#localhost:8000/api/book/1/reviews
class BookReview(View):
    def post(self, request, book_id):
        # Parse data from req.body (json)
        
        review_data=json.loads(request.body)
        review_data["book_id"]=book_id
        review_data["review_id"]=len(book_reviews)+1
        
        #Validate data using serializer
        review_serialized=BookReviewSerializer(data=review_data)
        if(review_serialized.is_valid()):
            book_reviews.append(review_serialized.data)

            return JsonResponse(review_serialized.data, status=201)
        else:
            return HttpResponseBadRequest()

class BookReviewUpdate(View):
    def put(self, request, review_id):

        #Parse data from req.body.
        review_data=json.loads(request.body)

        #Validate data
        review_serialized=BookReviewSerializer(data=review_data)
        if(review_serialized.is_valid()):
            # Find the review to update
            review_to_update=None
            for index, item in enumerate(book_reviews):
                if(item["review_id"]==review_id):
                    review_to_update=item
                    break
            
            # if data found, update it.
            if(review_to_update):
                book_reviews[index]=review_serialized.data
                return JsonResponse(review_serialized.data, status=200)
            
        return HttpResponseBadRequest()

class BookReviewDelete(View):
    def delete(self, request, review_id):
        for index, item in enumerate(book_reviews):
            if(item["review_id"]==review_id):
                book_reviews.remove(item)
                return JsonResponse("Review is deleted",safe=False,status=200)
        return HttpResponseBadRequest()

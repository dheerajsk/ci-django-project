
from django.urls import path
from .views import BookList, BookDetail, BookReview, BookReviewUpdate
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:book_id>/', BookDetail.as_view(), name='book-detail'),
    path('books/<int:book_id>/reviews', csrf_exempt(BookReview.as_view()), name='book-review'),
    path('reviews/<int:review_id>', csrf_exempt(BookReviewUpdate.as_view()), name='book-update')
]

from django.urls import path
from .views import BookList, BookDetail, BookReview, BookReviewUpdate, BookReviewDelete, UserSignIn, UserSignUp
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:book_id>/', BookDetail.as_view(), name='book-detail'),
    path('books/<int:book_id>/reviews', csrf_exempt(BookReview.as_view()), name='book-review'),
    path('reviews/<int:review_id>', csrf_exempt(BookReviewUpdate.as_view()), name='book-update'),
    path('reviews/<int:review_id>/delete', csrf_exempt(BookReviewDelete.as_view()), name='book-delete'),
    path('user/signup', csrf_exempt(UserSignUp.as_view()), name='user_signup'),
    path('user/signin', csrf_exempt(UserSignIn.as_view()), name='user_signin')
]
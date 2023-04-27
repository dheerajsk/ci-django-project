
from django.urls import path
from .views import BookList, BookDetail

urlpatterns=[
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:book_id>/', BookDetail.as_view(), name='book-detail')
]
from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Book, BookSerializer
# Create your views here.


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
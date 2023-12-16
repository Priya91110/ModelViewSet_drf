from django.db import models
from rest_framework import serializers
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=225)
    authorname = models.CharField(max_length=225)
    publishyear = models.IntegerField()
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
         
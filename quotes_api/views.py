from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, views, response
# Create your views here.
from quotes.models import Quote
from .serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticated]

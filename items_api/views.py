from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, views, response
# Create your views here.
from items.models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

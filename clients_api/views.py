from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from clients.models import Client
from .serializers import ClientSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
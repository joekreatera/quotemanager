from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, views, response
# Create your views here.
from clients.models import Client
from .serializers import ClientSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

class SpecialClientOps(views.APIView):

    def get(self, request):
        data = {"response1":"this is the response"}
        return response.Response(data)


    def post(self, request):
        instance = get_object_or_404(Client, id=2 )
        serial = ClientSerializer(instance, context={'request':request})
        return response.Response(serial.data)
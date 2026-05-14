from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from clients.models import Client

class ClientSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Client  
        fields = "__all__"
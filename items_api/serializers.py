from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from items.models import Item

class ItemSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Item  
        fields = "__all__"
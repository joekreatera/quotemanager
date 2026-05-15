from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from quotes.models import Quote

class QuoteSerializer(ModelSerializer):

    class Meta:
        model = Quote  
        fields = "__all__"
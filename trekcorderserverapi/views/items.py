"""View module for handling requests about Star Trek items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from trekcorderserverapi.models import Item
import stapi 

client = stapi.RestClient()

stapi_type = 'astronomicalObject'


class ItemView(ViewSet):
    """Trekcorder items"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            item = Item.objects.get(pk=pk)
            response = getattr(client, stapi_type).get(item.uid)
            serializer = ItemSerializer(item, context={'request': request})
            merged_response = {
                'my_data': serializer.data,
                'stapi': response.__dict__
            }
            return Response(merged_response)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
# Serializer 
class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for game types

    Arguments:
        serializers
    """
    class Meta:
        model = Item
        fields = ('id', 'name', 'uid')
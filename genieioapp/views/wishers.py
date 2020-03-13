from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Wisher


#from rest_framework.decorators import action

class WisherSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Wisher
        url = serializers.HyperlinkedIdentityField(
            view_name='wishers',
            lookup_field='id',
        )
        fields = ('id', 'user', 'cid')
        depth = 2
    
class Wishers(ViewSet):
    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer
        Returns:
            Response -- JSON serialized customer instance
        """

        try:
            wisher = Wisher.objects.get(pk=pk)
            serializer = WisherSerializer(wisher, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        """Handle GET requests to customers resource
        Returns:
            Response -- JSON serialized list of customers
        """      
       
        all_wishers = Wisher.objects.all()

        serializer = WisherSerializer(
                    all_wishers,
                    many=True,
                    context={'request': request}
                )
        serializer = WisherSerializer(all_wishers, many=True, context={'request': request})
        return Response(serializer.data)
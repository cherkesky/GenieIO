
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Location

class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Location
        url = serializers.HyperlinkedIdentityField(
            view_name='locations',
            lookup_field='id',
        )
        fields = ('id', 'location')
        depth = 2
        

class Locations(ViewSet):
    def retrieve(self, request, pk=None):
        """Handle GET requests for single word
        Returns:
            Response -- JSON serialized word instance
        """

        try:
            location = Locations.objects.get(pk=pk)
            serializer = LocationsSerializer(location, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        """Handle GET requests to words resource
        Returns:
            Response -- JSON serialized list of words
        """      
       
        all_locations = Location.objects.all()

        serializer = LocationsSerializer(
                    all_locations,
                    many=True,
                    context={'request': request}
                )
        serializer = LocationsSerializer(all_locations, many=True, context={'request': request})
        return Response(serializer.data)


   





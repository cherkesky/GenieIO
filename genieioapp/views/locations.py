
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Location
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Location
        url = serializers.HyperlinkedIdentityField(
            view_name='location',
            lookup_field='id',
        )
        fields = ('id', 'location')
        # depth = 2
        
class Locations(ViewSet):
    @method_decorator(csrf_exempt)
    def retrieve(self, request, pk=None):
        """Handle GET requests for single word
        Returns:
            Response -- JSON serialized word instance
        """
        try:
            location = Location.objects.get(pk=pk)
            serializer = LocationsSerializer(location, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    @method_decorator(csrf_exempt)
    def list(self, request):
        """Handle GET requests to words resource
        Returns:
            Response -- JSON serialized list of words
        """      
        get_state = self.request.query_params.get('get_state')

        if get_state:
            all_locations = Location.objects.filter(location__contains=get_state)
        else:
            all_locations = Location.objects.all()

        serializer = LocationsSerializer(
                    all_locations,
                    many=True,
                    context={'request': request}
                )
        serializer = LocationsSerializer(all_locations, many=True, context={'request': request})
        return Response(serializer.data)


   





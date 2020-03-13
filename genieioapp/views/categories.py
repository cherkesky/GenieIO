
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Category

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Category
        url = serializers.HyperlinkedIdentityField(
            view_name='categories',
            lookup_field='id',
        )
        fields = ('id', 'category')
        depth = 2
        

class Categories(ViewSet):
    def retrieve(self, request, pk=None):
        """Handle GET requests for single word
        Returns:
            Response -- JSON serialized word instance
        """

        try:
            category = Category.objects.get(pk=pk)
            serializer = CategoriesSerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        """Handle GET requests to words resource
        Returns:
            Response -- JSON serialized list of words
        """      
       
        all_categories = Category.objects.all()

        serializer = CategoriesSerializer(
                    all_categories,
                    many=True,
                    context={'request': request}
                )
        serializer = CategoriesSerializer(all_categories, many=True, context={'request': request})
        return Response(serializer.data)


   






from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Word

class WordsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Word
        url = serializers.HyperlinkedIdentityField(
            view_name='word',
            lookup_field='id',
        )
        fields = ('id', 'word')
        depth = 2
        

class Words(ViewSet):
    def retrieve(self, request, pk=None):
        """Handle GET requests for single word
        Returns:
            Response -- JSON serialized word instance
        """

        try:
            word = Word.objects.get(pk=pk)
            serializer = WordsSerializer(word, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        """Handle GET requests to words resource
        Returns:
            Response -- JSON serialized list of words
        """      
       
        all_words = Word.objects.all()

        serializer = WordsSerializer(
                    all_words,
                    many=True,
                    context={'request': request}
                )
        serializer = WordsSerializer(all_words, many=True, context={'request': request})
        return Response(serializer.data)


   





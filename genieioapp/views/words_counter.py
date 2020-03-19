
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Word_Counter
# from genieioapp.models import Wish_Word
# from django.db.models import Count

class WordCounterSerializer(serializers.HyperlinkedModelSerializer): 
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Word_Counter
        url = serializers.HyperlinkedIdentityField(
            view_name='word_counter',
            lookup_field='id',
        )
        fields = ('id', 'text', 'value')
        

class Words_Counter(ViewSet):

# handles GET one
    def retrieve(self, request, pk=None):
        """Handle GET requests for single word
        Returns:
            Response -- JSON serialized word instance
        """

        try:
            word_value = Word_Counter.objects.get(pk=pk)
            serializer = WordCounterSerializer(word_value, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
            
# handles GET all
    def list(self, request):
        """Handle GET requests to words resource
        Returns:
            Response -- JSON serialized list of words
        """ 
        # print("REQUEST",request)
        word_values = self.request.query_params.get('word_values')

        if word_values:
            all_wish_words = Word_Counter.objects.raw(" SELECT 1 as id, word.word as 'text', COUNT(ww.word_id) as 'value' FROM genieioapp_wish_word as ww JOIN genieioapp_word as word ON word.id = ww.word_id GROUP BY ww.word_id;")
            # all_wish_words = Wish_Word.objects.annotate(Count('word'))
        else:
            all_wish_words = Word_Counter.objects.all()

        serializer = WordCounterSerializer(
                    all_wish_words,
                    many=True,
                    context={'request': request}
                )
        return Response(serializer.data)


   





   





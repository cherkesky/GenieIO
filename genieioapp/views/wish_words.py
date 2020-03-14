
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Wish_Word
from genieioapp.models import Wish
from genieioapp.models import Word

class WishWordsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Wish_Word
        url = serializers.HyperlinkedIdentityField(
            view_name='wish_word',
            lookup_field='id',
        )
        fields = ('id', 'wish', 'word')
        depth = 1
        

class Wish_Words(ViewSet):

# handles GET one
    def retrieve(self, request, pk=None):
        """Handle GET requests for single word
        Returns:
            Response -- JSON serialized word instance
        """

        try:
            wish_word = Wish_Word.objects.get(pk=pk)
            serializer = WishWordsSerializer(wish_word, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

# handles GET all
    def list(self, request):
        """Handle GET requests to words resource
        Returns:
            Response -- JSON serialized list of words
        """      
       
        all_wish_words = Wish_Word.objects.all()

        serializer = WishWordsSerializer(
                    all_wish_words,
                    many=True,
                    context={'request': request}
                )
        serializer = WishWordsSerializer(all_wish_words, many=True, context={'request': request})
        return Response(serializer.data)

# handles POST
    def create(self, request):
            """Handle POST operations
            Returns:
            Response -- JSON serialized Products instance
            """

            new_wish_words = Wish_Word()
            new_wish_words.wish_id = request.data['wish']
            new_wish_words.word_id = request.data['word']

            new_wish_words.save()

            serializer = WishWordsSerializer(new_wish_words, context={'request': request})
            return Response(serializer.data)

   





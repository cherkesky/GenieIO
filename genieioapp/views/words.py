
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

# handles GET one
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
            
# handles GET all
    def list(self, request):
        """Handle GET requests to words resource
        Returns:
            Response -- JSON serialized list of words
        """ 
        # print("REQUEST",request)
        nltk = self.request.query_params.get('nltk', None)
    
        if nltk is not None:
            all_words = Word.objects.filter(word=nltk)
        else: 
            all_words = Word.objects.all()

        serializer = WordsSerializer(
                    all_words,
                    many=True,
                    context={'request': request}
                )
        print ("SERIALIZER", serializer.data)
        return Response(serializer.data)


# handles POST
    def create(self, request):
            """Handle POST operations
            Returns:
            Response -- JSON serialized Products instance
            """

            new_word = Word()
            new_word.word= request.data['word']

            new_word.save()

            serializer = WordsSerializer(new_word, context={'request': request})
            return Response(serializer.data)

   





   





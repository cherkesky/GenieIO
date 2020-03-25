from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Wish
from genieioapp.models import Category
from genieioapp.models import Location
from genieioapp.models import Wisher
from genieioapp.models import Word
from genieioapp.models import Wish_Word
from genieioapp.ntlk import harvest 

class WishesSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Wish
        url = serializers.HyperlinkedIdentityField(
            view_name='wish',
            lookup_field='id',
        )
        fields = ('id', 'wish_body', 'wisher', 'category', 'location','created_at')
        depth = 2
    
class Wishes(ViewSet):
    ntlk_wishes=[]

# handles GET one
    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer
        Returns:
            Response -- JSON serialized customer instance
        """
        try:
            wish = Wish.objects.get(pk=pk)
            serializer = WishesSerializer(wish, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

# handles GET all    
    def list(self, request):
        """Handle GET requests to customers resource
        Returns:
            Response -- JSON serialized list of customers
        """      
        search = self.request.query_params.get('search')
        latest = self.request.query_params.get('latest')
        my_wishes = self.request.query_params.get('my_wishes')

        if search:
         all_wishes = Wish.objects.filter(wish_body__contains=search).exclude(wisher_id=self.request.user.id)

        elif latest:
          all_wishes = Wish.objects.order_by('-created_at').exclude(wisher_id=self.request.user.id)[0:int(latest)]
          print (all_wishes)
        elif my_wishes:
          all_wishes = Wish.objects.filter(wisher_id=self.request.user.id)
        else:
          all_wishes = Wish.objects.all()

        serializer = WishesSerializer(
                    all_wishes,
                    many=True,
                    context={'request': request}
                )
        serializer = WishesSerializer(all_wishes, many=True, context={'request': request})
        return Response(serializer.data)

# handles POST
    def create(self, request):
            """Handle POST operations
            Returns:
            Response -- JSON serialized Products instance
            """
            new_wish = Wish()
            wish_for_harvesting = ""
            new_wish.wisher_id = request.auth.user.wisher.id
            new_wish.wish_body = request.data['wish_body']
            new_wish.category_id = request.data['category']
            new_wish.location_id = request.data['location']
            new_wish.save()
        #  NLTK for getting all the relevant keywords
            ntlk_wishes = harvest(new_wish.wish_body)
            print ("NLTK", ntlk_wishes)
        # Iterating through the results and building the Word and Wish_Word tables
            for ntlk_wish in ntlk_wishes:
                try:
                     response = Word.objects.filter(word=ntlk_wish)
                     if len(response) > 0:
                         print ("The word",ntlk_wish, "been found in index:", response[0].id)
                         new_wish_word = Wish_Word()
                         new_wish_word.wish_id = new_wish.pk
                         new_wish_word.word_id = response[0].id
                         new_wish_word.save()

                     else:
                          # building the words table for missing words
                          print ("The word",ntlk_wish, "has not been found")
                          new_word = Word()
                          new_word.word= ntlk_wish
                          new_word.save() 
                          print ("The word",ntlk_wish, "been added to the Word table")
                          new_wish_word = Wish_Word()
                          new_wish_word.wish_id = new_wish.pk
                          new_wish_word.word_id = new_word.pk
                          new_wish_word.save()
                except Exception as ex:
                     return HttpResponseServerError(ex)
                
            serializer = WishesSerializer(new_wish, context={'request': request})
            return Response(serializer.data)

# handles DELETE
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single product

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            wish_del = Wish.objects.get(pk=pk)
            # restrict users to only being able to delete wishes they've created
            if wish_del.wisher_id == request.auth.user.wisher.id:
                wish_del.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except wish_del.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# handles PUT
    def update(self, request, pk=None):
        """Handle PUT requests for a product

        Returns:
        Response -- Empty body with 204 status code
        """
        wish_update = Wish.objects.get(pk=pk)      
        wish_update.wisher_id = request.auth.user.wisher.id
        wish_update.wish_body = request.data['wish_body']
        wish_update.category_id = request.data['category']
        wish_update.location_id = request.data['location']
        
        wish_update.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)



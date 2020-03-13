from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Wish
from genieioapp.models import Category
from genieioapp.models import Location
from genieioapp.models import Wisher


#from rest_framework.decorators import action

class WishesSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Wish
        url = serializers.HyperlinkedIdentityField(
            view_name='wishes',
            lookup_field='id',
        )
        fields = ('id', 'wisher', 'wish_body', 'category', 'location','created_at', )
        depth = 2
    
class Wishes(ViewSet):
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
    
    def list(self, request):
        """Handle GET requests to customers resource
        Returns:
            Response -- JSON serialized list of customers
        """      
       
        all_wishes = Wish.objects.all()

        serializer = WishesSerializer(
                    all_wishes,
                    many=True,
                    context={'request': request}
                )
        serializer = WishesSerializer(all_wishes, many=True, context={'request': request})
        return Response(serializer.data)


    # def create(self, request):
    #         """Handle POST operations
    #         Returns:
    #         Response -- JSON serialized Products instance
    #         """

    #         new_wish = Wishes()
    #         new_wish.wisher_id = request.auth.user.wisher.id
    #         new_wish.wish_body = request.data['wish_body']
    #         new_wish.wish_body = request.data['category']
    #         new_wish.wish_body = request.data['location']
    #         new_wish.wish_body = request.data['wish_body']

    #         new_wish.save()

    #         serializer = WishesSerializer(new_wish, context={'request': request})

    #         return Response(serializer.data)







    #Custom action to update user profile
    # @action(methods=['put'], detail=False)
    # def profile_update(self, request):
    #     """
    #     Handle PUT requests for a customer
    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     customer = Customer.objects.get(pk=request.auth.user.customer.id)
    #     # customer.user.id = request.auth.user.customer.id
    #     customer.address = request.data["address"]
    #     # accesses the nested users last name
    #     customer.user.last_name = request.data["last_name"]
    #     customer.user.first_name = request.data["first_name"]
    #     customer.save()
    #     customer.user.save()
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)
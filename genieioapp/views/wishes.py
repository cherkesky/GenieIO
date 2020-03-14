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
            view_name='wish',
            lookup_field='id',
        )
        fields = ('id', 'wish_body', 'wisher', 'category', 'location','created_at')
        depth = 2
    
class Wishes(ViewSet):

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
            new_wish.wisher_id = request.auth.user.wisher.id
            new_wish.wish_body = request.data['wish_body']
            new_wish.category_id = request.data['category']
            new_wish.location_id = request.data['location']

            new_wish.save()

        #####################################################################
        ## INSERT LOGIC FOR NTLK AND CREATING RELEVANT WORD TABLES HERE    ##
        #####################################################################

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
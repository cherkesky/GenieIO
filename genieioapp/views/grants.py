from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from genieioapp.models import Grant
from genieioapp.models import Wish
from genieioapp.models import Wisher
#from rest_framework.decorators import action


class GrantsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for grants
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Grant
        url = serializers.HyperlinkedIdentityField(
            view_name='grant',
            lookup_field='id',
        )
        fields = ('id', 'granter', 'wish', 'memo', 'status', 'created_at')
        depth = 1


class Grants(ViewSet):

    # handles GET one
    def retrieve(self, request, pk=None):
        """Handle GET requests for single grants
        Returns:
            Response -- JSON serialized grants instance
        """
        try:
            grant = Grant.objects.get(pk=pk)
            serializer = GrantsSerializer(grant, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

# handles GET all
    def list(self, request):
        """Handle GET requests to grants resource
        Returns:
            Response -- JSON serialized list of grants
        """
        by_wish = self.request.query_params.get('by_wish')
        relevant_wish = self.request.user.id
        if by_wish:
            all_grants = Grant.objects.raw(f' SELECT g.id, g.memo, g.status, g.wish_id, g.granter_id, w.wisher_id FROM genieioapp_grant AS g JOIN genieioapp_wish AS w ON g.wish_id = w.id WHERE w.wisher_id={relevant_wish}; ')

        else:
            all_grants = Grant.objects.all()

        serializer = GrantsSerializer(
            all_grants,
            many=True,
            context={'request': request}
        )
        serializer = GrantsSerializer(
            all_grants, many=True, context={'request': request})
        return Response(serializer.data)

# handles POST
    def create(self, request):
        """Handle POST operations
        Returns:
        Response -- JSON serialized grant instance
        """

        new_grant = Grant()
        new_grant.granter_id = request.auth.user.wisher.id
        new_grant.wish_id = request.data['wish_id']
        new_grant.memo = request.data['memo']
        new_grant.status = request.data['status']

        new_grant.save()

        serializer = GrantsSerializer(new_grant, context={'request': request})
        return Response(serializer.data)

# handles DELETE
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single grant

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            grant_del = Grant.objects.get(pk=pk)
            # restrict users to only being able to delete wishes they've created
            if grant_del.wisher_id == request.auth.user.wisher.id:
                grant_del.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except grant_del.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# handles PUT
    def update(self, request, pk=None):
        """Handle PUT requests for a grant

        Returns:
        Response -- Empty body with 204 status code
        """
        grant_update = Grant.objects.get(pk=pk)
        grant_update.wisher_id = request.auth.user.wisher.id
        grant_update.wish_id = request.data['wish']
        grant_update.memo = request.data['memo']
        grant_update.status = request.data['status']

        grant_update.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

# handles PATCH

    def partial_update(self, request, pk=None):
        """Handle PATCH requests for a grant
        Returns:
            Response -- Empty body with 204 status code
        """
        grant_update = Grant.objects.get(pk=pk)
        grant_update.status = request.data['status']

        grant_update.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

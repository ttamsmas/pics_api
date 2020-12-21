from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.like import Like
from ..serializers import LikeSerializer, UserSerializer

# Create your views here.
class Likes(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = LikeSerializer
    def get(self, request):
        """Index request"""
        # Get all the likes:
        likes = Like.objects.all()
        # Run the data through the serializer
        data = LikeSerializer(likes, many=True).data
        return Response({ 'likes': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['like']['owner'] = request.user.id
        # Serialize/create like
        like = LikeSerializer(data=request.data['like'])
        # If the like data is valid according to our serializer...
        if like.is_valid():
            # Save the created like & send a response
            like.save()
            return Response({ 'like': like.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(like.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def delete(self, request, pk):
        """Delete request"""
        # Locate like to delete
        like = get_object_or_404(Like, pk=pk)
        # Check the like's owner agains the user making this request
        if not request.user.id == like.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this like')
        # Only delete if the user owns the  like
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['like'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['like'].get('owner', False):
            del request.data['like']['owner']

        # Locate Like
        # get_object_or_404 returns a object representation of our Like
        like = get_object_or_404(Like, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == like.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this like')

        # Add owner to data object now that we know this user owns the resource
        request.data['like']['owner'] = request.user.id
        # Validate updates with serializer
        data = LikeSerializer(like, data=request.data['like'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

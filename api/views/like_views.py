from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.like import Like
from ..serializers import LikeSerializer, UserSerializer, LikeReadSerializer

# Create your views here.
class Likes(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = LikeSerializer
    def get(self, request):
        """Index request"""
        # Get all the likes:
        likes = Like.objects.all()
        # Run the data through the serializer
        data = LikeReadSerializer(likes, many=True).data
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

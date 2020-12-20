from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.pic import Pic
from ..serializers import PicSerializer, UserSerializer

# Create your views here.
class Pics(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PicSerializer
    def get(self, request):
        """Index request"""
        # Get all the pics:
        # pics = Pic.objects.all()
        # Filter the pics by owner, so you can only see your owned pics
        # May want to change how this line works to allow users to see all pics from accounts they follow
        pics = Pic.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = PicSerializer(pics, many=True).data
        return Response({ 'pics': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['pic']['owner'] = request.user.id
        # Serialize/create pic
        pic = PicSerializer(data=request.data['pic'])
        # If the pic data is valid according to our serializer...
        if pic.is_valid():
            # Save the created pic & send a response
            pic.save()
            return Response({ 'pic': pic.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(pic.errors, status=status.HTTP_400_BAD_REQUEST)

class PicDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the pic to show
        pic = get_object_or_404(Pic, pk=pk)
        # Only want to show owned pics?
        if not request.user.id == pic.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this pic')

        # Run the data through the serializer so it's formatted
        data = PicSerializer(pic).data
        return Response({ 'pic': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate pic to delete
        pic = get_object_or_404(Pic, pk=pk)
        # Check the pic's owner agains the user making this request
        if not request.user.id == pic.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this pic')
        # Only delete if the user owns the  pic
        pic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['pic'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['pic'].get('owner', False):
            del request.data['pic']['owner']

        # Locate Pic
        # get_object_or_404 returns a object representation of our Pic
        pic = get_object_or_404(Pic, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == pic.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this pic')

        # Add owner to data object now that we know this user owns the resource
        request.data['pic']['owner'] = request.user.id
        # Validate updates with serializer
        data = PicSerializer(pic, data=request.data['pic'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

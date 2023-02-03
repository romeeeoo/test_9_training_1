from rest_framework import viewsets, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from gallery.models import Picture


# Create your views here.

class FavouriteApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(request.user)
        picture_id = data.get("picture_id")
        picture = Picture.objects.get(pk=picture_id)
        print(picture)
        if request.user.favorite_pictures.filter(pk=picture_id):
            print("picture to be removed")
            request.user.favorite_pictures.remove(picture)
            print("picture removed from favourite")
            return Response(status=203)
        else:
            request.user.favorite_pictures.add(picture)
            print("picture added to favourite")
            return Response(status=201)


# class FavouriteApiView(viewsets.ModelViewSet):
#     pass







from rest_framework.response import Response
from rest_framework.views import APIView

from gallery.models import Picture


# Create your views here.

class FavoriteApiView(APIView):
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
            return Response()
        else:
            request.user.favorite_pictures.add(picture)
            print("picture added to favourite")
            return Response()







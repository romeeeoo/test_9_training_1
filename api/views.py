import datetime

from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CommentSerializer
from gallery.models import Picture, Comment


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


class CreateCommentApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(request.data)
        picture_id = data.get("picture_id")
        text = data.get("text")
        author_id = request.user.pk
        serializer = CommentSerializer(
            data={
                "text": text,
                "picture": picture_id,
                "author": author_id,
                "datetime_created": datetime.datetime.now()
            })
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        print(serializer.errors)
        return Response(status=500)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request,  *args, **kwargs):
        data = request.data
        print(data)
        picture_id = data.get("picture_id")
        text = data.get("text")
        author_id = request.user.pk
        request_data = {
                "text": text,
                "picture": picture_id,
                "author": author_id,
                "datetime_created": datetime.datetime.now()}
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DeleteCommentApiView(APIView):
    def delete(self, request, *args, **kwargs):
        data = request.data
        comment_id = data.get("comment_id")
        comment = Comment.objects.filter(pk=comment_id)
        if comment:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)



from django.contrib.auth import get_user_model
from rest_framework import serializers

from gallery.models import Comment, Picture


class PictureFavouredBySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    picture_id = serializers.PrimaryKeyRelatedField(read_only=True)


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=200, required=True)
    picture = serializers.PrimaryKeyRelatedField(queryset=Picture.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    datetime_created = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class PictureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    description = serializers.CharField(max_length=300, required=True)
    created_at = serializers.DateTimeField(read_only=True)
    favored_by = PictureFavouredBySerializer(many=True)
    comments = CommentSerializer(many=True)









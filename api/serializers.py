from rest_framework import serializers


class PictureFavouredBySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    picture_id = serializers.PrimaryKeyRelatedField(read_only=True)

class PictureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    description = serializers.CharField(max_length=300, required=True)
    created_at = serializers.DateTimeField(read_only=True)
    favored_by = PictureFavouredBySerializer(many=True)

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=200, required=True)
    picture = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    datetime_created = serializers.DateTimeField(read_only=True)





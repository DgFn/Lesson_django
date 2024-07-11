from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        publisher_user = serializers.HiddenField(
            default=serializers.CurrentUserDefault(),
            source='user', )

    likes = serializers.SerializerMethodField()

    @extend_schema_field(serializers.IntegerField)
    def get_likes(self, obj):
        return obj.like_comment.count()


class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('post',)

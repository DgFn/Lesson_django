from django.contrib.auth.models import User
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from likes.models import Like
from tms_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'user', 'is_published')

    likes = serializers.SerializerMethodField()

    @extend_schema_field(serializers.IntegerField)
    def get_likes(self, obj):
        return obj.likes.count()


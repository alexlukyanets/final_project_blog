from rest_framework import serializers
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    views = serializers.ReadOnlyField(default=0)

    class Meta:
        model = Post
        fields = '__all__'

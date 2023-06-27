from rest_framework import serializers
from post.models import Post, PostLikeUnlike


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text')


class PostGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'user_id')


class PostLikeUnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikeUnlike
        fields = ('post_id', 'reaction')


class PostLikeUnlikeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikeUnlike
        fields = ('post_id', 'user_id', 'reaction')

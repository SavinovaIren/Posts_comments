from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from social.models import Comment, Post

User = get_user_model()


class CommentSerializer(ModelSerializer):
    creator = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ['id', 'text_comment', 'creator', 'created', 'updated', 'post']

from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from social.models import Post, Comment
from social.permissions import PermissionPolicyMixin, IsAdminOrOwner
from social.serializers.comment_serializer import CommentSerializer
from social.serializers.post_serializer import PostSerializer
from social.serializers.user_serializer import UserSerializer

User = get_user_model()


class UserViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_per_method = {
        "list": [IsAdminUser | IsAuthenticated],
        "create": [AllowAny],
        "update": [IsAdminOrOwner],
        "destroy": [IsAdminUser],
        "retrieve": [IsAdminOrOwner],
    }


class PostViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "create": [IsAuthenticated],
        "update": [IsAdminOrOwner],
        "destroy": [IsAdminOrOwner],
        "retrieve": [AllowAny],
    }

class CommentViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "create": [IsAuthenticated],
        "update": [IsAdminOrOwner],
        "destroy": [IsAdminOrOwner],
        "retrieve": [AllowAny]
    }

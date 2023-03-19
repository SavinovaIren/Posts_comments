from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from social.models import Post, Comment
from social.serializers.comment_serializer import CommentSerializer
from social.serializers.post_serializer import PostSerializer
from social.serializers.user_serializer import UserSerializer

User = get_user_model()


# class UserViewSet(PermissionPolicyMixin, ModelViewSet):
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes_per_method = {
    #     "list": [IsAdminUser],
    #     "create": [AllowAny],
    #     "update": ((IsOwner | IsAdminUser),),
    #     "destroy": ((IsOwner | IsAdminUser),),
    #     "retrieve": ((IsOwner | IsAdminUser),),
    # }

# class BookViewSet(PermissionPolicyMixin, ModelViewSet):
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes_per_method = {
    #     "list": [AllowAny],
    #     "create": [IsAdminUser],
    #     "update": [IsAdminUser],
    #     "destroy": [IsAdminUser],
    #     "retrieve": [AllowAny],
    # }

# class AuthorViewSet(PermissionPolicyMixin, ModelViewSet):
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes_per_method = {
    #     "list": [AllowAny],
    #     "create": [IsAdminUser],
    #     "update": [IsAdminUser],
    #     "destroy": [IsAdminUser],
    #     "retrieve": [AllowAny]
    # }

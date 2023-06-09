from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from social.models import Post, Comment
from social.serializers.comment_serializer import CommentSerializer

User = get_user_model()


class TitleValidator:
    def __call__(self, value):
        banned_words = ['ерунда', 'глупость', 'чепуха']
        for word in banned_words:
            if word in value.lower():
                raise serializers.ValidationError(
                    f"Слова {', '.join([word for word in banned_words])} не могут быть в заголовке")
        return value


class PostSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    comments = serializers.SerializerMethodField()
    title = serializers.CharField(validators=[TitleValidator()])

    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, value):
        author_age = value.get("author")
        if author_age.birth_date is None:
            raise serializers.ValidationError("Поле возраста должно быть заполнено")
        age = (timezone.now().date() - author_age.birth_date).days // 365
        if age < 18:
            raise serializers.ValidationError("Посты могут писать только пользователи старше 18 лет")
        else:
            return value

    def get_comments(self, obj):
        queryset = Comment.objects.filter(post=obj.id)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data

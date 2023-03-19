from django.contrib.auth.models import AbstractUser
from django.db import models

from Posts_comments import settings


class User(AbstractUser):
    phone = models.BigIntegerField(verbose_name="Номер телефона")
    birth_date = models.DateField(null=False, editable=False, blank=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        app_label = 'social'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=25)
    text = models.TextField(verbose_name="Текст")
    photo = models.ImageField(upload_to="media/", verbose_name="Фото", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор поста', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    comments = models.ManyToManyField('Comment', related_name='comment', blank=True)

    class Meta:
        app_label = 'social'
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    text_comment = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.creator} написал под статьей {self.post.title}: {self.text_comment}'

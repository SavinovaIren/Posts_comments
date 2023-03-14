from django.contrib.auth.models import AbstractUser
from django.db import models

from Posts_comments import settings


class User(AbstractUser):
    phone = models.BigIntegerField(verbose_name="Номер телефона")
    birth_date = models.DateField(null=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.PROTECT)
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"



class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=25)
    text = models.TextField(verbose_name="Текст")
    photo = models.ImageField(upload_to="media/", verbose_name="Фото", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, verbose_name='Автор', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"




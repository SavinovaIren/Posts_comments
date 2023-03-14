from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html

from social.models import Post, Comment

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'phone', 'birth_date', 'updated', 'date_joined')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'photo', 'author_link', 'comment',
                    'updated', 'created')
    list_filter = ('created',)

    def author_link(self, obj):
        author = obj.author
        url = reverse("admin:social_author_changelist") + str(author.pk)
        return format_html(f'<a href="{url}"> {author} </a>')

    author_link.short_description = "Автор"


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'updated', 'created')


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.urls import reverse
from urllib.parse import quote as urlquote
from django.contrib.admin.utils import quote
from social.models import Post, Comment

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'phone', 'birth_date', 'updated', 'date_joined')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'photo', 'author_link',
                    'updated', 'created')
    list_filter = ('created',)

    def author_link(self, obj):
        auth = obj.author
        url = reverse("admin:social_user_changelist") + str(auth.pk)
        return format_html(f'<a href="{url}">{auth}</a>')

    author_link.short_description = "Автор"



class CommentAdmin(admin.ModelAdmin):
    list_display = ('creator', 'text_comment', 'updated', 'created', 'post')


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

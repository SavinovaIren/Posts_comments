# Generated by Django 4.1.7 on 2023-03-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_alter_comment_creator_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comment', to='social.comment'),
        ),
    ]
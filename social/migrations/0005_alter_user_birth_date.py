# Generated by Django 4.1.7 on 2023-03-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=545),
            preserve_default=False,
        ),
    ]

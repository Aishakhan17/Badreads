# Generated by Django 4.2.3 on 2023-07-21 18:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0044_rename_books_review_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='running_head',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

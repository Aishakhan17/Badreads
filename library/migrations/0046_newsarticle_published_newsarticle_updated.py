# Generated by Django 4.2.3 on 2023-07-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0045_newsarticle_running_head_alter_newsarticle_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='published',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

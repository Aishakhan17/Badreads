# Generated by Django 4.2.3 on 2023-07-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_rename_bookimg_book_image_alter_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-29 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0065_alter_group_image_alter_newsarticle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

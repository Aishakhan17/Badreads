# Generated by Django 4.2.3 on 2023-07-29 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0066_alter_newsarticle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

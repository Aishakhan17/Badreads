# Generated by Django 4.2.3 on 2023-07-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0049_alter_newsarticle_running_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

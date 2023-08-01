# Generated by Django 4.2.3 on 2023-07-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0029_user_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currently_reading',
            field=models.ManyToManyField(blank=True, related_name='currently_reading', to='library.book'),
        ),
        migrations.AddField(
            model_name='user',
            name='want_to_read',
            field=models.ManyToManyField(blank=True, related_name='want_to_read', to='library.book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='read', to='library.book'),
        ),
    ]
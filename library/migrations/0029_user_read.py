# Generated by Django 4.2.3 on 2023-07-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0028_delete_bookshelf'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='read',
            field=models.ManyToManyField(blank=True, to='library.book'),
        ),
    ]
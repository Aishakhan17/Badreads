# Generated by Django 4.2.3 on 2023-07-21 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0046_newsarticle_published_newsarticle_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.message'),
        ),
    ]

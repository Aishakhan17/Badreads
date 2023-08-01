# Generated by Django 4.2.3 on 2023-07-18 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0036_alter_userbook_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbook',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='userbooks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.userbook'),
        ),
        migrations.AlterField(
            model_name='userbook',
            name='book_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userbook',
            name='rating',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-16 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0035_remove_user_books_book_users_userbook_book_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.book'),
        ),
    ]

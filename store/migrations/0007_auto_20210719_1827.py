# Generated by Django 2.2.1 on 2021-07-19 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_book_numreviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='numreviews',
            new_name='num_of_reviews',
        ),
    ]

# Generated by Django 2.2.1 on 2021-07-17 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210717_0651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',), 'verbose_name': 'Book'},
        ),
        migrations.AlterModelOptions(
            name='bookcopy',
            options={'verbose_name': 'Book Copy'},
        ),
    ]

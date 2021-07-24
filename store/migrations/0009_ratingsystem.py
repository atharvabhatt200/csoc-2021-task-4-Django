# Generated by Django 2.2.1 on 2021-07-22 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_auto_20210719_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rated', models.BooleanField(default=False)),
                ('rating', models.SmallIntegerField(default=None)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Book')),
                ('rated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

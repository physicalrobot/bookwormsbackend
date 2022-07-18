# Generated by Django 4.0.5 on 2022-07-18 19:56

import BooksApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('BookId', models.AutoField(primary_key=True, serialize=False)),
                ('BookTitle', models.CharField(max_length=500)),
                ('BookCover', models.ImageField(blank=True, null=True, upload_to=BooksApp.models.upload_path)),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-21 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='booktitle',
            new_name='reviewtitle',
        ),
    ]
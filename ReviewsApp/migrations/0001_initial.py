# Generated by Django 4.0.5 on 2022-07-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('ReviewId', models.AutoField(primary_key=True, serialize=False)),
                ('ReviewBook', models.CharField(max_length=500)),
                ('ReviewBody', models.CharField(max_length=500)),
                ('ReviewRating', models.CharField(max_length=500)),
            ],
        ),
    ]

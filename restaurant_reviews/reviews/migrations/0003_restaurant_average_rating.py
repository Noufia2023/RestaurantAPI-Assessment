# Generated by Django 4.2.3 on 2023-07-23 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]
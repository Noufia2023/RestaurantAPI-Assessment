# Generated by Django 4.2.2 on 2023-07-15 13:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField()),
                ('restaurant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.restaurant')),
            ],
        ),
    ]
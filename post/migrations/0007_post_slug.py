# Generated by Django 5.0.6 on 2024-07-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-11 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]

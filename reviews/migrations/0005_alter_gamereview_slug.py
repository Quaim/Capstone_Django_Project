# Generated by Django 4.2.11 on 2024-03-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_gamereview_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
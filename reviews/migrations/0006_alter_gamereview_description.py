# Generated by Django 4.2.11 on 2024-03-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_gamereview_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]

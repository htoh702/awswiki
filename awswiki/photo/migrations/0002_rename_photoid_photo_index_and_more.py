# Generated by Django 4.2 on 2024-04-22 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photoId',
            new_name='index',
        ),
        migrations.RenameField(
            model_name='photo_reviews',
            old_name='photoId',
            new_name='index',
        ),
    ]
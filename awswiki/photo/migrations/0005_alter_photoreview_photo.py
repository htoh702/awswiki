# Generated by Django 4.2 on 2024-04-23 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_alter_photoreview_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoreview',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='photo.photo'),
        ),
    ]

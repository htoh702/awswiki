# Generated by Django 4.2 on 2024-04-22 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_rename_photoid_photo_index_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(null=True, upload_to='Photo/images/'),
        ),
        migrations.DeleteModel(
            name='photo_reviews',
        ),
        migrations.AddField(
            model_name='photoreview',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='photo.photo'),
        ),
    ]

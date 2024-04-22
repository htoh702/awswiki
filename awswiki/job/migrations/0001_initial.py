# Generated by Django 4.2 on 2024-04-22 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('jobId', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True, max_length=50)),
                ('image', models.FileField(null=True, upload_to='job/images/')),
            ],
        ),
        migrations.CreateModel(
            name='job_reviews',
            fields=[
                ('jobReviewId', models.AutoField(primary_key=True, serialize=False)),
                ('reivew', models.CharField(max_length=50)),
                ('jobId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_job_description_jobs_job_description_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='job_description_en',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='job_description_original',
        ),
        migrations.AddField(
            model_name='jobs',
            name='job_name_arabic',
            field=models.CharField(default='', max_length=200),
        ),
    ]
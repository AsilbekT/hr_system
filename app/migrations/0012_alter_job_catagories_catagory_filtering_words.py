# Generated by Django 4.1.3 on 2022-11-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_catagory_jobs_catagory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_catagories',
            name='catagory_filtering_words',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-28 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_group_name_job_catagories_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=2001)),
                ('job_url', models.URLField()),
                ('job_date', models.DateField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.job_catagories')),
            ],
        ),
    ]

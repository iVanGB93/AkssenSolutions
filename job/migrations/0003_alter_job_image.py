# Generated by Django 5.0.2 on 2024-02-29 00:23

import job.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_amount_spent_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(default='jobs/jobDefault.jpg', upload_to=job.models.upload_to_job),
        ),
    ]

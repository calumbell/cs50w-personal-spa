# Generated by Django 3.2 on 2021-06-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeitem',
            name='bulletPoints',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='resumeitem',
            name='summary',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]

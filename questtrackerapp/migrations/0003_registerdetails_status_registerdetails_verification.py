# Generated by Django 4.0.7 on 2022-12-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questtrackerapp', '0002_registerdetails_delete_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdetails',
            name='Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registerdetails',
            name='Verification',
            field=models.CharField(default='', max_length=20),
        ),
    ]

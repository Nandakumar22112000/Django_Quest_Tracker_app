# Generated by Django 4.0.7 on 2023-01-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questtrackerapp', '0015_assignprojecttoteam_submit'),
    ]

    operations = [
        migrations.CreateModel(
            name='createteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_Name', models.CharField(max_length=20)),
                ('Manager', models.CharField(max_length=20)),
            ],
        ),
    ]

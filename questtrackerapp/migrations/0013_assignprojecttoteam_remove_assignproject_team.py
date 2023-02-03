# Generated by Django 4.0.7 on 2023-01-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questtrackerapp', '0012_assignproject_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignprojecttoteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Name', models.CharField(max_length=40)),
                ('Project', models.FileField(upload_to='')),
                ('Deadline', models.DateField()),
                ('Team', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='assignproject',
            name='Team',
        ),
    ]

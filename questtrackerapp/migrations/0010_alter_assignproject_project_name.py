# Generated by Django 4.0.7 on 2022-12-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questtrackerapp', '0009_assignproject_project_name_registerdetails_teamlead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignproject',
            name='Project_Name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]

# Generated by Django 4.0.7 on 2022-12-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questtrackerapp', '0005_assignproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignproject',
            name='Deadline',
            field=models.DateField(null=True),
        ),
    ]

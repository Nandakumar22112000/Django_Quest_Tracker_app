# Generated by Django 4.0.7 on 2023-01-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questtrackerapp', '0011_alter_registerdetails_teamlead'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignproject',
            name='Team',
            field=models.CharField(default='', max_length=20),
        ),
    ]

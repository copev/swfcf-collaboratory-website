# Generated by Django 3.1.7 on 2021-03-20 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaboratory_api', '0009_auto_20210320_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='cause_id',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='region_id',
        ),
    ]

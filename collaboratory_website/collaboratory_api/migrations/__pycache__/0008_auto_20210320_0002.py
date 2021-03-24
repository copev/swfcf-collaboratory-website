# Generated by Django 3.1.7 on 2021-03-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaboratory_api', '0007_auto_20210317_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='cause_id',
            field=models.ManyToManyField(blank=True, db_column='CauseID', related_name='organization', to='collaboratory_api.Cause'),
        ),
        migrations.AddField(
            model_name='organization',
            name='org_id',
            field=models.AutoField(db_column='OrgID', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='ein',
            field=models.IntegerField(db_column='EIN'),
        ),
        migrations.RemoveField(
            model_name='organization',
            name='region_id',
        ),
        migrations.AddField(
            model_name='organization',
            name='region_id',
            field=models.ManyToManyField(blank=True, db_column='RegionID', related_name='organization', to='collaboratory_api.Region'),
        ),
    ]

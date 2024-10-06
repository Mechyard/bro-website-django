# Generated by Django 5.0.8 on 2024-09-29 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bro_theme', '0004_sectionmodel_is_inner'),
        ('cms', '0035_auto_20230822_2208_squashed_0036_auto_20240311_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterMenuModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('start_level', models.IntegerField(blank=True, default=0)),
                ('end_level', models.IntegerField(blank=True, default=100)),
                ('extra_inactive', models.IntegerField(blank=True, default=2)),
                ('extra_active', models.IntegerField(blank=True, default=2)),
                ('title', models.CharField(default='', max_length=127)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
    ]

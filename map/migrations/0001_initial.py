# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sno', models.CharField(max_length=4)),
                ('tot', models.PositiveSmallIntegerField()),
                ('sbi', models.PositiveSmallIntegerField()),
                ('mday', models.DateTimeField()),
                ('bemp', models.PositiveSmallIntegerField()),
                ('act', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sno', models.CharField(max_length=4)),
                ('sna', models.CharField(max_length=128)),
                ('sarea', models.CharField(max_length=128)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('ar', models.CharField(max_length=128)),
                ('sareaen', models.CharField(max_length=256)),
                ('snaen', models.CharField(max_length=256)),
                ('aren', models.CharField(max_length=256)),
            ],
        ),
    ]

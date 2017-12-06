# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0008_auto_20171129_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='start_time',
        ),
        migrations.AddField(
            model_name='shift',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 22, 26, 52, 48932, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='shift',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 22, 26, 52, 48856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='run',
            name='covered',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0010_auto_20171130_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='shiftGroup',
        ),
        migrations.AlterField(
            model_name='shift',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 22, 40, 31, 52072, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shift',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 22, 40, 31, 52011, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='ShiftGroup',
        ),
    ]

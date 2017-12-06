# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0005_remove_shift_covered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='start_datetime',
        ),
        migrations.AddField(
            model_name='shift',
            name='end_date',
            field=models.DateField(default=b'2015-01-01'),
        ),
        migrations.AddField(
            model_name='shift',
            name='end_time',
            field=models.TimeField(default="06:30:00"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='start_date',
            field=models.DateField(default=b'2015-01-01'),
        ),
        migrations.AddField(
            model_name='shift',
            name='start_time',
            field=models.TimeField(default="08:30:00"),
            preserve_default=False,
        ),
    ]

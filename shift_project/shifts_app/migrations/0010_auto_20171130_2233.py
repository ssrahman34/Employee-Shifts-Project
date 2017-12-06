# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0009_auto_20171130_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='shift',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 22, 33, 40, 939060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shift',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 22, 33, 40, 939020, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='shift',
            name='shiftGroup',
            field=models.ForeignKey(related_name='shifts_related', blank=True, to='shifts_app.ShiftGroup', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0011_auto_20171201_2240'),
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
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 22, 43, 3, 434515, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shift',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 22, 43, 3, 434476, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='shift',
            name='shiftGroup',
            field=models.ForeignKey(related_name='shifts_related', blank=True, to='shifts_app.ShiftGroup', null=True),
        ),
    ]

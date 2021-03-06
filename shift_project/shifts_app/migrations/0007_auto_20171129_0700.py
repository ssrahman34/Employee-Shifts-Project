# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0006_auto_20171129_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 29, 7, 0, 4, 909841, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shift',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 29, 7, 0, 4, 909894, tzinfo=utc)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='Shift',
        ),
        migrations.AddField(
            model_name='run',
            name='shift',
            field=models.ForeignKey(related_name='runs_related', blank=True, to='shifts_app.Shift', null=True),
        ),
    ]

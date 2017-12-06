# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0004_run_covered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='covered',
        ),
    ]

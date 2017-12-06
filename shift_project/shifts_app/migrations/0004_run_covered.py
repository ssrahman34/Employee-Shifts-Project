# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0003_shift_covered'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='covered',
            field=models.BooleanField(default=True),
        ),
    ]

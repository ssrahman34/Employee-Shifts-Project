# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0002_auto_20171119_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='covered',
            field=models.BooleanField(default=True),
        ),
    ]

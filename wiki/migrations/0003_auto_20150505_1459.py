# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20150505_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rozdil',
            name='is_main',
            field=models.BooleanField(default=1, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xb8\xd0\xb9 ?'),
        ),
    ]

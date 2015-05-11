# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rozdil',
            name='is_main',
            field=models.BooleanField(default=1, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xb8\xd0\xb9 \xd1\x87\xd0\xb8 \xd0\xb4\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbc\xd1\x96\xd0\xb6\xd0\xbd\xd0\xb8\xd0\xb9.'),
        ),
    ]

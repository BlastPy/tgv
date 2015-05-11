# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20150508_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='robota',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

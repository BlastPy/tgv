# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20150505_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rozdil',
            name='part_of',
            field=models.ForeignKey(verbose_name=b'\xd0\x92 \xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8\xd0\xbd\xd1\x96', to='wiki.NamePart'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='main_is',
            field=models.ForeignKey(verbose_name=b'\xd0\x97 \xd1\x80\xd0\xbe\xd0\xb7\xd0\xb4\xd1\x96\xd0\xbb\xd1\x83', to='wiki.Rozdil'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='name',
            field=models.CharField(max_length=170, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xb8\xd0\xb9 ?'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='opus_ustanovku',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81 \xd1\x83\xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='robota',
            field=models.TextField(verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xbe\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='teh_obslug',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd1\x85\xd0\xbd\xd1\x96\xd1\x87\xd0\xbd\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb2\xd1\x83\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='tth',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xa2\xd0\xa5'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='zag_bund',
            field=models.TextField(verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0 \xd0\xb1\xd1\x83\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0'),
        ),
    ]

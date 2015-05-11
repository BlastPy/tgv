# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NamePart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba \xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb8.')),
            ],
        ),
        migrations.CreateModel(
            name='Rozdil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb7\xd0\xb4\xd1\x96\xd0\xbb\xd1\x83')),
                ('is_main', models.BooleanField(default=0, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xb8\xd0\xb9 \xd1\x87\xd0\xb8 \xd0\xb4\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbc\xd1\x96\xd0\xb6\xd0\xbd\xd0\xb8\xd0\xb9.')),
                ('part_of', models.ForeignKey(to='wiki.NamePart')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=170)),
                ('image', models.ImageField(upload_to=b'media')),
                ('robota', models.TextField()),
                ('opus_ustanovku', models.TextField()),
                ('zag_bund', models.TextField()),
                ('tth', models.TextField()),
                ('teh_obslug', models.TextField()),
                ('main_is', models.ForeignKey(to='wiki.Rozdil')),
            ],
        ),
    ]

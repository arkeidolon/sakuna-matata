# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150808_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 8, 9, 15, 9, 824758, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 8, 9, 15, 15, 406424, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

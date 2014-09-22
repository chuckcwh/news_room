# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_news_news_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=b'North America', max_length=20, choices=[(b'North America', b'North America'), (b'South America', b'South America'), (b'Asia', b'Asia'), (b'Europe', b'Europe'), (b'Africa', b'Africa'), (b'Australia', b'Australia')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NA', max_length=2, choices=[(b'NA', b'North America'), (b'SA', b'South America'), (b'AS', b'Asia'), (b'EU', b'Europe'), (b'AF', b'Africa'), (b'AU', b'Australia')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('news_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('news_text', models.TextField()),
                ('category', models.ForeignKey(related_name=b'news', to='news.Category')),
                ('user', models.ForeignKey(related_name=b'news', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

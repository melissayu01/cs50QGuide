# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='date_time',
        ),
        migrations.AddField(
            model_name='club',
            name='abbreviation',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='overall_rating',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=1),
        ),
        migrations.AddField(
            model_name='club',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2015, 11, 29, 4, 25, 30, 66304, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='club',
            name='genre',
        ),
        migrations.AddField(
            model_name='club',
            name='genre',
            field=models.ManyToManyField(to='search.Genre'),
        ),
    ]

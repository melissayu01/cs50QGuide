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
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('abbreviation', models.CharField(max_length=10, blank=True)),
                ('description', models.TextField(max_length=2000)),
                ('website', models.URLField(blank=True)),
                ('overall_rating', models.DecimalField(null=True, max_digits=2, decimal_places=1, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.IntegerField(choices=[(1, b'Science'), (2, b'Math'), (3, b'Service'), (4, b'Publications'), (5, b'Sports'), (6, b'Finance'), (7, b'Culture'), (8, b'Dance')])),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('review', models.TextField(max_length=2000)),
                ('name', models.ForeignKey(to='search.Club')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='genre',
            field=models.ManyToManyField(to='search.Genre'),
        ),
    ]

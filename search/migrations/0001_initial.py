# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('game_id', models.CharField(max_length=10, null=True, blank=True)),
                ('platform', models.CharField(max_length=200, null=True, blank=True)),
                ('genre', models.CharField(max_length=200, null=True, blank=True)),
                ('release_date', models.DateField(null=True, blank=True)),
                ('overview', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_type', models.CharField(max_length=50, choices=[(b'fanart', b'Fan Art'), (b'boxart', b'Box Art'), (b'banner', b'Banner'), (b'screenshot', b'Screen Shot'), (b'clearlogo', b'Clear Logo')])),
                ('url', models.URLField()),
                ('width', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('thumb', models.URLField(null=True, blank=True)),
                ('side', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

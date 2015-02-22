# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20141222_1010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Question2',
        ),
    ]

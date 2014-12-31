# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20141222_1012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question2',
            new_name='Question',
        ),
    ]

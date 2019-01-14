# -*- coding: utf-8 -*-

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dts_test_app', '0002_test_drop_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='DummyModel',
            name='indexed_value',
            field=models.CharField(max_length=255, db_index=True),
        ),
    ]

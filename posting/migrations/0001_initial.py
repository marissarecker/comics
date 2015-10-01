# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComicStrip',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, unique=True)),
                ('title', models.CharField(max_length=120)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'title', editable=False)),
                ('date', models.DateField()),
                ('image_url', models.URLField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

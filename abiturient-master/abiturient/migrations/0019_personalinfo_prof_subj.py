# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0018_remove_personalinfo_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='prof_subj',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name=''),
        ),
    ]

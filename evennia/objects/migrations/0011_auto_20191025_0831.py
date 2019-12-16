# Generated by Django 2.2.6 on 2019-10-25 12:31

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0010_auto_20190128_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectdb',
            name='db_sessid',
            field=models.CharField(help_text='csv list of session ids of connected Account, if any.', max_length=32, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='session id'),
        ),
        migrations.AlterField(
            model_name='objectdb',
            name='db_typeclass_path',
            field=models.CharField(db_index=True, help_text="this defines what 'type' of entity this is. This variable holds a Python path to a module with a valid Evennia Typeclass.", max_length=255, null=True, verbose_name='typeclass'),
        ),
    ]
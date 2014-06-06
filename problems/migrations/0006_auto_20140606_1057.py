# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='language_family',
            field=models.ForeignKey(to_field='id', default=1, to='problems.LanguageFamily'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='problem',
            name='language',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='author',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='source',
        ),
        migrations.AlterField(
            model_name='attempt',
            name='is_successful',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='note',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]

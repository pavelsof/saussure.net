# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_auto_20140606_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('family', models.ForeignKey(to_field='id', to='problems.LanguageFamily')),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='problem',
            name='source',
            field=models.CharField(max_length=240, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.CharField(max_length=240, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='problem',
            name='language',
            field=models.ForeignKey(to='problems.Language', blank=True, null=True, to_field='id'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='problem',
            name='language_family',
        ),
        migrations.AlterField(
            model_name='problem',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='is_successful',
            field=models.BooleanField(default=False),
        ),
    ]

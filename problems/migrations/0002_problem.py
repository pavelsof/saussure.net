# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=240)),
                ('language', models.ForeignKey(to='problems.Language', to_field='id')),
                ('author', models.CharField(max_length=240)),
                ('source', models.CharField(max_length=240)),
                ('text', models.TextField()),
                ('note', models.TextField(blank=True, null=True)),
                ('number_of_challenges', models.PositiveSmallIntegerField(default=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='problems.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

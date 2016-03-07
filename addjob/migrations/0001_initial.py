# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Wybierz w jakiej branzy pracujesz.', unique=True, max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'branze',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EngJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Polska nazwa Twojego stanowiska', unique=True, max_length=100, verbose_name='Angielska nazwa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Polska nazwa Twojego stanowiska', unique=True, max_length=100, verbose_name='Polska nazwa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opis', models.TextField(help_text='Na czym polega Twoja praca?', max_length=1000, verbose_name='opis stanowiska')),
                ('dzien', models.TextField(help_text='Co robiles przez 8 godzin w pracy?', max_length=1000, verbose_name='opis dnia')),
                ('slug', models.SlugField()),
                ('branza', models.ForeignKey(related_name='branza_requests_created', to='addjob.Branza')),
                ('eng_job', models.ForeignKey(verbose_name='Angielska nazwa', to='addjob.EngJob')),
                ('pl_job', models.ForeignKey(verbose_name='Polska nazwa', to='addjob.PlJob')),
                ('sektor', models.ForeignKey(related_query_name='br', related_name='sektors_requests_created', to='addjob.Branza')),
            ],
            options={
                'verbose_name_plural': 'stanowiska',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Z czym kojarzy Ci sie Twoja praca', unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stanowisko',
            name='tags',
            field=models.ManyToManyField(related_name='tags_request_created', to='addjob.Tags'),
            preserve_default=True,
        ),
    ]

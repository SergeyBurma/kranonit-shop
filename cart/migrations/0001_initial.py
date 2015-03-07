# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(verbose_name='Opened at', auto_now_add=True)),
                ('closed_at', models.DateTimeField(blank=True, verbose_name='Closed at', null=True)),
                ('is_closed', models.BooleanField(default=False, verbose_name='Is closed')),
                ('is_processed', models.BooleanField(default=False, verbose_name='Is processed')),
                ('phone', models.CharField(max_length=32, null=True)),
                ('address', models.CharField(max_length=256, null=True)),
                ('name', models.CharField(verbose_name='Contact name', max_length=64, null=True)),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'verbose_name': 'Order',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderPosition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(related_name='positions', to='cart.Order')),
                ('product', models.ForeignKey(to='catalog.Product')),
            ],
            options={
                'verbose_name_plural': 'Order positions',
                'verbose_name': 'Order position',
                'ordering': ['-count'],
            },
            bases=(models.Model,),
        ),
    ]

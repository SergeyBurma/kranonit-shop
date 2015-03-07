# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'verbose_name': 'Product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='catalog.ProductCategory'),
            preserve_default=True,
        ),
    ]

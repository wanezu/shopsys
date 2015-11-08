# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', help_text='根据name生成的，用于生成页面URL,必须唯一')),
                ('description', models.TextField(verbose_name='描述')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('meta_keywords', models.CharField(max_length=255, verbose_name='Mate关键词', help_text='mate关键词，有利于SEO，用逗号分隔')),
                ('meta_description', models.CharField(max_length=255, verbose_name='Meta描述', help_text='meta描述')),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'categories',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='名称')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', help_text='根据name生成的，用于生成页面URL,必须唯一')),
                ('brand', models.CharField(max_length=50, verbose_name='品牌')),
                ('sku', models.CharField(max_length=50, verbose_name='计量单位')),
                ('price', models.DecimalField(max_digits=9, decimal_places=2, verbose_name='价格')),
                ('old_price', models.DecimalField(default=0.0, max_digits=9, decimal_places=2, verbose_name='旧价格', blank=True)),
                ('image', models.ImageField(max_length=50, verbose_name='图片', upload_to='')),
                ('is_active', models.BooleanField(default=True, verbose_name='设为激活')),
                ('is_bestseller', models.BooleanField(default=False, verbose_name='标为畅销')),
                ('is_featured', models.BooleanField(default=False, verbose_name='标为推荐')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('description', models.TextField(verbose_name='描述')),
                ('meta_keywords', models.CharField(max_length=255, verbose_name='Mate关键词', help_text='mate关键词，有利于SEO，用逗号分隔')),
                ('meta_description', models.CharField(max_length=255, verbose_name='Meta描述', help_text='meta描述')),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'products',
            },
        ),
    ]

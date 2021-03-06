# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(blank=True, max_length=1500)),
                ('status', models.CharField(max_length=10)),
                ('first_published', models.DateTimeField(verbose_name='first published')),
                ('last_edited', models.DateTimeField(verbose_name='last edited')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=12)),
                ('short_desc', models.TextField(blank=True, max_length=150)),
                ('created_on', models.DateTimeField(verbose_name='created on')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.User'),
        ),
    ]

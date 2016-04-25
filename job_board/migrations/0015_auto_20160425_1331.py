# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0014_auto_20160419_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_range', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_board.Salary'),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Diner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('tlf', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='MEDIA_ROOT')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=255)),
                ('occupied', models.BooleanField(default=False)),
                ('diner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Diner')),
            ],
        ),
        migrations.CreateModel(
            name='UserWorksAtDiner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Diner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Table'),
        ),
    ]

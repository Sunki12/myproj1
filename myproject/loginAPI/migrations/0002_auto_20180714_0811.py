# Generated by Django 2.0.7 on 2018-07-14 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='account',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_bound_qq',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_bound_wechat',
        ),
        migrations.RemoveField(
            model_name='users',
            name='qq_account',
        ),
        migrations.RemoveField(
            model_name='users',
            name='wechat_account',
        ),
    ]
# Generated by Django 2.0.7 on 2018-07-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FM', '0002_auto_20180714_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_bound_qq',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_bound_wechat',
            field=models.BooleanField(default=False),
        ),
    ]

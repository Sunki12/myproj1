# Generated by Django 2.0.7 on 2018-07-16 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginAPI', '0002_auto_20180714_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('per_taste', models.CharField(max_length=20)),
                ('per_meat', models.CharField(max_length=20)),
                ('per_vege', models.CharField(max_length=20)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginAPI.Users')),
            ],
        ),
    ]

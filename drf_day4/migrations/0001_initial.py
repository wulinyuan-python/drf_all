# Generated by Django 2.0.6 on 2020-11-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '工人',
                'verbose_name_plural': '工人',
                'db_table': 'bz_workers',
            },
        ),
    ]

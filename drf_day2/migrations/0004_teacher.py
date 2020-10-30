# Generated by Django 2.0.6 on 2020-10-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_day2', '0003_auto_20201028_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=64)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('pic', models.ImageField(default='pic/1.jpg', upload_to='pic/')),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
                'db_table': 'teacher',
            },
        ),
    ]
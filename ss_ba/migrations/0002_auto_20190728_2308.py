# Generated by Django 2.2.1 on 2019-07-28 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss_ba', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='lookup',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='up_date',
        ),
    ]

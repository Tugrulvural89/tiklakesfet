# Generated by Django 2.0 on 2017-12-31 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messblog', '0008_auto_20171231_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file1',
        ),
    ]

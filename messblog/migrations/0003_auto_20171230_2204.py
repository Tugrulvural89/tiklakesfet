# Generated by Django 2.0 on 2017-12-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messblog', '0002_auto_20171230_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
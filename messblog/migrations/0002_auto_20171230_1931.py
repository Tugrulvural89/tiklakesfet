# Generated by Django 2.0 on 2017-12-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
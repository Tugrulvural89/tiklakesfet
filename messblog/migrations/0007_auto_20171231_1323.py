# Generated by Django 2.0 on 2017-12-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messblog', '0006_auto_20171231_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='file1',
            field=models.FilePathField(blank=True, null=True),
        ),
    ]

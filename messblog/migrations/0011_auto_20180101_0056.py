# Generated by Django 2.0 on 2017-12-31 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messblog', '0010_remove_post_image4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='post',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/jpeg/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='static/jpeg/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/jpeg/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/jpeg/'),
        ),
    ]
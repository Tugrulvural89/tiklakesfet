# Generated by Django 2.0 on 2018-01-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messblog', '0011_auto_20180101_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(blank=True, max_length=75, verbose_name='user email')),
                ('imported', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2021-10-30 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20211030_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
    ]
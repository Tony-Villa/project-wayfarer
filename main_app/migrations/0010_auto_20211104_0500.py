# Generated by Django 3.1.2 on 2021-11-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20211103_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.CharField(default='https://images.unsplash.com/photo-1601922047316-70884dbbde2f?ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y2hpY2FnbyUyMG5pZ2h0fGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=60', max_length=1024),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=255),
        ),
    ]

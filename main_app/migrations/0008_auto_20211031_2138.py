# Generated by Django 3.1.2 on 2021-10-31 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_comment_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='profile',
        ),
        migrations.AddField(
            model_name='blog',
            name='profile',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='main_app.profile'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_profile_post_count_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post_count',
        ),
        migrations.AddField(
            model_name='profile',
            name='posts',
            field=models.ManyToManyField(to='blog.post'),
        ),
    ]

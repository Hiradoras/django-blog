# Generated by Django 4.0.3 on 2022-03-31 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_profile_date_joined_alter_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-11 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_comment_commentor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentor',
            new_name='user',
        ),
    ]

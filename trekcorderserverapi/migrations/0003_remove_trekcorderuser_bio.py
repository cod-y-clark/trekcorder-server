# Generated by Django 4.0.3 on 2022-03-16 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trekcorderserverapi', '0002_rename_username_trekcorderuser_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trekcorderuser',
            name='bio',
        ),
    ]

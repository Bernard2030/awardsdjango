# Generated by Django 3.2.8 on 2021-10-24 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_awards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rates',
            old_name='userbility',
            new_name='usability',
        ),
    ]

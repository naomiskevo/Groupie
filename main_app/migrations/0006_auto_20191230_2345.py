# Generated by Django 2.2.6 on 2019-12-30 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20191230_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_url',
            new_name='url',
        ),
    ]
# Generated by Django 2.2.6 on 2020-01-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]

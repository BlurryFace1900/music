# Generated by Django 3.2.9 on 2022-01-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='votes_to_skil',
            new_name='votes_to_skip',
        ),
    ]

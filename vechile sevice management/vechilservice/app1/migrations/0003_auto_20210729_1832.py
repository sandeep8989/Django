# Generated by Django 3.2.5 on 2021-07-29 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_custname_show_customername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='customerName',
            new_name='VECHILETYPE',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='vechtype',
            new_name='cutomerName',
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-04 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesaccounts', '0006_auto_20180420_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalsaleslead',
            old_name='Probability',
            new_name='probability',
        ),
        migrations.RenameField(
            model_name='saleslead',
            old_name='Probability',
            new_name='probability',
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesaccounts', '0007_auto_20180504_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_executive',
            field=models.BooleanField(default=False, verbose_name='Executive'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_management',
            field=models.BooleanField(default=False, verbose_name='Mangement'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_top40',
            field=models.BooleanField(default=False, verbose_name='Top 40 Account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='account',
            name='relationship_status',
            field=models.CharField(choices=[(3, 'Super'), (2, 'Good'), (1, 'Okay'), (0, 'Worrying')], default=2, max_length=256),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='is_executive',
            field=models.BooleanField(default=False, verbose_name='Executive'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='is_management',
            field=models.BooleanField(default=False, verbose_name='Mangement'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='is_top40',
            field=models.BooleanField(default=False, verbose_name='Top 40 Account'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='relationship_status',
            field=models.CharField(choices=[(3, 'Super'), (2, 'Good'), (1, 'Okay'), (0, 'Worrying')], default=2, max_length=256),
        ),
    ]
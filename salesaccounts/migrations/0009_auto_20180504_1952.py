# Generated by Django 2.0.5 on 2018-05-04 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salesaccounts', '0008_auto_20180504_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_management',
            field=models.BooleanField(default=False, verbose_name='Management'),
        ),
        migrations.AlterField(
            model_name='account',
            name='relationship_status',
            field=models.CharField(choices=[('3', 'Super'), ('2', 'Good'), ('1', 'Okay'), ('0', 'Worrying')], default='2', max_length=256),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='is_management',
            field=models.BooleanField(default=False, verbose_name='Management'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='relationship_status',
            field=models.CharField(choices=[('3', 'Super'), ('2', 'Good'), ('1', 'Okay'), ('0', 'Worrying')], default='2', max_length=256),
        ),
        migrations.AlterField(
            model_name='historicalsaleslead',
            name='est_decision_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Estimated close date'),
        ),
        migrations.AlterField(
            model_name='saleslead',
            name='est_decision_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Estimated close date'),
        ),
        migrations.AlterField(
            model_name='saleslead',
            name='pm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='salesaccounts.CREmployee', verbose_name='Project Manager'),
        ),
    ]
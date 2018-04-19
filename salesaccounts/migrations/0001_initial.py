# Generated by Django 2.0.4 on 2018-04-19 08:03

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('sector', models.CharField(max_length=256)),
                ('relationship_status', models.CharField(choices=[('1', 'Super'), ('2', 'Good'), ('3', 'Okay'), ('4', 'Worrying')], default='2', max_length=256)),
                ('region', models.CharField(max_length=256)),
                ('is_top40', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), editable=False)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='AccountGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('user_account', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('accountperson_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='salesaccounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('path', models.TextField(default='')),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
            ],
        ),
        migrations.CreateModel(
            name='CREmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('short_name', models.CharField(max_length=256)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), editable=False)),
                ('user_account', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CR Employee',
                'verbose_name_plural': 'CR Employees',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAccount',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('sector', models.CharField(max_length=256)),
                ('relationship_status', models.CharField(choices=[('1', 'Super'), ('2', 'Good'), ('3', 'Okay'), ('4', 'Worrying')], default='2', max_length=256)),
                ('region', models.CharField(max_length=256)),
                ('is_top40', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('account_group', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='salesaccounts.AccountGroup')),
                ('account_manager', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='salesaccounts.CREmployee')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Account',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAccountGroup',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical account group',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCREmployee',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('short_name', models.CharField(max_length=256)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical CR Employee',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalPerson',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('lastname', models.CharField(max_length=256)),
                ('firstname', models.CharField(max_length=256)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Person',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSalesLead',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Open'), ('2', 'Won'), ('3', 'Lost')], default='1', max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('service_group', models.CharField(blank=True, max_length=256, null=True)),
                ('competitors', models.CharField(blank=True, max_length=256, null=True)),
                ('partners', models.CharField(blank=True, max_length=256, null=True)),
                ('CRM_id', models.CharField(blank=True, max_length=256, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, null=True)),
                ('created_on_date', models.DateField(default=django.utils.timezone.now, editable=False, null=True)),
                ('name', models.CharField(max_length=256)),
                ('est_decision_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Probability', models.IntegerField(default=50, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('contact', models.CharField(blank=True, max_length=256, null=True)),
                ('status_reason', models.CharField(blank=True, max_length=256)),
                ('actual_close_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('actual_close_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, null=True)),
                ('est_revenue_GBP', models.FloatField()),
                ('description', models.TextField(blank=True, default='Product:-\nCompetition:-\nPartners:-\nCompelling reason:-\nNext steps:-\n', null=True)),
                ('next_action', models.TextField(blank=True, default='', null=True)),
                ('next_action_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='salesaccounts.Account')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='salesaccounts.CREmployee')),
                ('sales_originator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='salesaccounts.CREmployee')),
            ],
            options={
                'verbose_name': 'historical Sales Lead',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalServiceType',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('service_type', models.CharField(max_length=256)),
                ('service_name', models.TextField(default='')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical service type',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('meeting_schedule', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('user_account', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Meeting',
                'verbose_name_plural': 'Meetings',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('meeting_schedule', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('meetingminutes_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='salesaccounts.Meeting')),
                ('user_account', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MeetingMinutes',
                'verbose_name_plural': 'MeetingMinutes',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=256)),
                ('firstname', models.CharField(max_length=256)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_account', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('user_account', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesLead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Open'), ('2', 'Won'), ('3', 'Lost')], default='1', max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('service_group', models.CharField(blank=True, max_length=256, null=True)),
                ('competitors', models.CharField(blank=True, max_length=256, null=True)),
                ('partners', models.CharField(blank=True, max_length=256, null=True)),
                ('CRM_id', models.CharField(blank=True, max_length=256, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, null=True)),
                ('created_on_date', models.DateField(default=django.utils.timezone.now, editable=False, null=True)),
                ('name', models.CharField(max_length=256)),
                ('est_decision_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Probability', models.IntegerField(default=50, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('contact', models.CharField(blank=True, max_length=256, null=True)),
                ('status_reason', models.CharField(blank=True, max_length=256)),
                ('actual_close_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('actual_close_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, null=True)),
                ('est_revenue_GBP', models.FloatField()),
                ('description', models.TextField(blank=True, default='Product:-\nCompetition:-\nPartners:-\nCompelling reason:-\nNext steps:-\n', null=True)),
                ('next_action', models.TextField(blank=True, default='', null=True)),
                ('next_action_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='salesaccounts.Account')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='salesaccounts.CREmployee')),
                ('sales_originator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='salesaccounts.CREmployee')),
            ],
            options={
                'verbose_name': 'Sales Lead',
                'verbose_name_plural': 'Sales Leads',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('scheduled', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('user_account', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('meeting_schedule', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_deleted', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('scheduledemployee_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='salesaccounts.Schedule')),
                ('user_account', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=256)),
                ('service_name', models.TextField(default='')),
                ('user_account', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='saleslead',
            name='service_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='salesaccounts.ServiceType'),
        ),
        migrations.AddField(
            model_name='saleslead',
            name='user_account',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalsaleslead',
            name='service_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='salesaccounts.ServiceType'),
        ),
        migrations.AddField(
            model_name='historicalsaleslead',
            name='user_account',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attachment',
            name='attachment_meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='salesaccounts.Meeting'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='user_account',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accountperson',
            name='accountperson_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='salesaccounts.Person'),
        ),
        migrations.AddField(
            model_name='accountperson',
            name='user_account',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='account_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='salesaccounts.AccountGroup'),
        ),
        migrations.AddField(
            model_name='account',
            name='account_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='salesaccounts.CREmployee'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_account',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionEvents',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('event_name', models.CharField(max_length=255, verbose_name='event name')),
                ('event_message', models.CharField(max_length=255, verbose_name='event message')),
            ],
            options={
                'db_table': 'events',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ExecutionResults',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('hosts', models.CharField(max_length=255, verbose_name='list of hosts for this execution')),
                ('results', models.TextField(verbose_name='json  string for execution')),
            ],
            options={
                'db_table': 'results',
                'managed': True,
            },
        ),
    ]
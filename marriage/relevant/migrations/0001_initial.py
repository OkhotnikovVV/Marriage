# Generated by Django 5.0.3 on 2024-04-17 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(default=18)),
                ('gender', models.CharField(default='m', max_length=1)),
                ('city', models.CharField(default='city', max_length=10)),
                ('amount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_from', models.PositiveIntegerField(default=0)),
                ('level_to', models.PositiveIntegerField(default=0)),
                ('percent', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('people', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='relevant.people')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('phd', models.FloatField(default=0.0)),
                ('higher_education', models.FloatField(default=0.0)),
                ('undergraduate_education', models.FloatField(default=0.0)),
                ('secondary_professional_education', models.FloatField(default=0.0)),
                ('secondary_education', models.FloatField(default=0.0)),
                ('basic_education', models.FloatField(default=0.0)),
                ('primary_education', models.FloatField(default=0.0)),
                ('pre_school_education', models.FloatField(default=0.0)),
                ('without_education', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('people', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='relevant.people')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('married', models.FloatField(default=0.0)),
                ('single', models.FloatField(default=0.0)),
                ('divorced', models.FloatField(default=0.0)),
                ('separation', models.FloatField(default=0.0)),
                ('widowed', models.FloatField(default=0.0)),
            ],
        ),
    ]

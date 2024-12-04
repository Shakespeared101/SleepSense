# Generated by Django 5.1.3 on 2024-11-21 16:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stress_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SleepData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.IntegerField()),
                ('body_movements', models.IntegerField()),
                ('respiratory_rate', models.IntegerField()),
                ('eeg_data', models.FloatField()),
                ('sleeping_hours', models.FloatField()),
                ('blood_oxygen_level', models.IntegerField()),
                ('snoring_rate', models.IntegerField()),
                ('limb_movement_rate', models.IntegerField()),
                ('stress_level', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

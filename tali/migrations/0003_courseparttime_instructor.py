# Generated by Django 4.0.4 on 2022-05-21 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tali', '0002_coursefulltime_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseparttime',
            name='instructor',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='tali.instructor'),
        ),
    ]
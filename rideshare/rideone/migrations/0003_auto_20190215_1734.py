# Generated by Django 2.0.10 on 2019-02-15 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rideone', '0002_auto_20190215_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='vehicl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rideone.vehicle'),
        ),
    ]

# Generated by Django 4.0 on 2022-04-01 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_payment_appointmentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='patientID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.patient'),
        ),
    ]

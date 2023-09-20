# Generated by Django 4.0 on 2022-04-01 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_payment_patientid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='mode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='testID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.test'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

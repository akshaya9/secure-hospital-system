# Generated by Django 4.0.3 on 2022-04-02 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_payment_mode_alter_payment_testid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='diagnosisID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.diagnosis'),
        ),
    ]

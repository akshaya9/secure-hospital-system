# Generated by Django 3.0.5 on 2022-03-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='paymentID',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Payment'),
        ),
    ]

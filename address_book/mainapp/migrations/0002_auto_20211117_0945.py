# Generated by Django 3.2.9 on 2021-11-17 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.address'),
        ),
    ]

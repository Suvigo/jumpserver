# Generated by Django 2.1.4 on 2018-12-07 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0023_auto_20181016_1650'),
        ('ops', '0003_auto_20181207_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='adhoc',
            name='run_as',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.SystemUser'),
        ),
    ]

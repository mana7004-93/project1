# Generated by Django 2.2.5 on 2019-11-22 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0005_auto_20191122_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='prodid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='productapp.Product'),
        ),
    ]
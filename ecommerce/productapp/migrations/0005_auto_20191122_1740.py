# Generated by Django 2.2.5 on 2019-11-22 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_auto_20191105_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='prodid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='productapp.Product'),
        ),
    ]
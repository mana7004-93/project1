# Generated by Django 2.2.5 on 2019-10-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pcat', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
                ('discount', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
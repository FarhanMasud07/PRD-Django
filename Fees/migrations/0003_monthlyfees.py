# Generated by Django 3.0.5 on 2020-04-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fees', '0002_delete_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyFees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.CharField(max_length=15)),
                ('MonthlyDate', models.DateField(auto_now=True)),
                ('StudentName', models.CharField(max_length=100)),
                ('Class', models.CharField(max_length=5)),
                ('Section', models.CharField(max_length=10)),
                ('Special', models.FloatField(default=0)),
                ('FeesType', models.CharField(max_length=10)),
                ('Ammount', models.FloatField()),
            ],
        ),
    ]

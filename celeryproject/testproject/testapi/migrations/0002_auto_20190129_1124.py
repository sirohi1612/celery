# Generated by Django 2.1.5 on 2019-01-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]

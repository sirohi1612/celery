# Generated by Django 2.1.5 on 2019-01-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0003_auto_20190129_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

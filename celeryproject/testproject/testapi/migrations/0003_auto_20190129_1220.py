# Generated by Django 2.1.5 on 2019-01-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0002_auto_20190129_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

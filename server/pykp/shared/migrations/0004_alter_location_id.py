# Generated by Django 5.0 on 2023-12-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_location_id_alter_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

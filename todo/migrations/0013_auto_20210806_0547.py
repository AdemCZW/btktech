# Generated by Django 3.2.5 on 2021-08-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_flight_pd_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='pd_content',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='pd_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
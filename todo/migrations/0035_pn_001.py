# Generated by Django 3.2.5 on 2021-09-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0034_price_003_price_004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pn_001',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pn_ph_001', models.CharField(default='圖片連結', max_length=1000)),
            ],
        ),
    ]

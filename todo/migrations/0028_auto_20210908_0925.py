# Generated by Django 3.2.5 on 2021-09-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0027_auto_20210903_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio_001',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_ph_001', models.CharField(default='SOME STRING', max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_ph_001',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_ph_002',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_ph_003',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_ph_004',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_ph_005',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_ph_006',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_001',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_002',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_003',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_004',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_005',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_006',
            field=models.CharField(max_length=100),
        ),
    ]

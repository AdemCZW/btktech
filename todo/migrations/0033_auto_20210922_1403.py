# Generated by Django 3.2.5 on 2021-09-22 14:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0032_remove_price_001_price_tit_001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price_002',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_btn_002', models.CharField(default='按鈕名稱', max_length=1000)),
                ('price_txt_002', ckeditor.fields.RichTextField(blank=True, default='輸入文字敘述', max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_001',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_002',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_003',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_004',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_005',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='index_001',
            name='mid_txt_006',
            field=models.TextField(max_length=100),
        ),
    ]
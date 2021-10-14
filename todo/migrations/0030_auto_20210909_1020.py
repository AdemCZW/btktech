# Generated by Django 3.2.5 on 2021-09-09 10:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0029_auto_20210909_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price_001',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_btn_001', models.CharField(default='按鈕名稱', max_length=1000)),
                ('price_txt_001', ckeditor.fields.RichTextField(blank=True, default='輸入文字敘述', max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='service_001',
            name='service_ph_001',
            field=models.CharField(default='圖片連結', max_length=1000),
        ),
        migrations.AlterField(
            model_name='studio_001',
            name='studio_ph_001',
            field=models.CharField(default='圖片連結', max_length=1000),
        ),
    ]
# Generated by Django 3.2.5 on 2023-03-07 10:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ffmm_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ffmm_tit', models.CharField(blank=True, max_length=1000, verbose_name='產品標題')),
                ('ffmm_num', models.CharField(blank=True, max_length=1000, verbose_name='產品型號')),
                ('ffmm_img', models.CharField(blank=True, max_length=1000, verbose_name='產品圖片')),
                ('ffmm_det', ckeditor.fields.RichTextField(blank=True, default='產品規格', max_length=10000, null=True, verbose_name='內容')),
            ],
            options={
                'verbose_name': 'file folder',
                'verbose_name_plural': 'file folder',
            },
        ),
        migrations.CreateModel(
            name='home_poly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poly_index_001', models.CharField(blank=True, max_length=1000, verbose_name='文字')),
                ('poly_index_002', models.CharField(blank=True, max_length=1000, verbose_name='輪播圖片-1')),
                ('poly_index_003', models.CharField(blank=True, max_length=1000, verbose_name='輪播圖片-2')),
                ('poly_index_004', models.CharField(blank=True, max_length=1000, verbose_name='輪播圖片-3')),
                ('poly_index_005', models.CharField(blank=True, max_length=1000, verbose_name='輪播圖片-4')),
                ('poly_index_006', models.CharField(blank=True, max_length=1000, verbose_name='輪播圖片-5')),
            ],
            options={
                'verbose_name': 'poly-home',
                'verbose_name_plural': 'poly-home',
            },
        ),
    ]

# Generated by Django 3.2.5 on 2022-03-18 12:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herrmann', '0005_auto_20220318_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_cont_03',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_img_002',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_img_003',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_img_004',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_img_005',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_seri_002',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_seri_003',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_seri_004',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_seri_005',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_seri_cont_002',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_seri_cont_003',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_seri_cont_004',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_seri_cont_005',
        ),
        migrations.RemoveField(
            model_name='welding_02',
            name='welding_tit_02',
        ),
        migrations.AlterField(
            model_name='welding_01',
            name='welding_txt_001',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, verbose_name='產品特色內容-1'),
        ),
        migrations.AlterField(
            model_name='welding_01',
            name='welding_txt_002',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, verbose_name='產品特色內容-2'),
        ),
        migrations.AlterField(
            model_name='welding_01',
            name='welding_txt_003',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, verbose_name='產品特色內容-3'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_cont',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, verbose_name='主要產品說明'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_seri_001_1',
            field=ckeditor.fields.RichTextField(blank=True, default='文字敘述', max_length=10000, null=True, verbose_name='內容'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_seri_001_2',
            field=ckeditor.fields.RichTextField(blank=True, default='文字敘述', max_length=10000, null=True, verbose_name='內容'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_seri_001_3',
            field=ckeditor.fields.RichTextField(blank=True, default='文字敘述', max_length=10000, null=True, verbose_name='內容'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_seri_001_4',
            field=ckeditor.fields.RichTextField(blank=True, default='文字敘述', max_length=10000, null=True, verbose_name='內容'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_seri_001_tit_01',
            field=models.CharField(blank=True, max_length=1000, verbose_name='產品系列-標題-1'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_seri_001_tit_02',
            field=models.CharField(blank=True, max_length=1000, verbose_name='產品系列-標題-2'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_seri_001_tit_03',
            field=models.CharField(blank=True, max_length=1000, verbose_name='產品系列-標題-3'),
        ),
        migrations.AlterField(
            model_name='welding_02',
            name='welding_seri_001_tit_04',
            field=models.CharField(blank=True, max_length=1000, verbose_name='產品系列-標題-4'),
        ),
    ]

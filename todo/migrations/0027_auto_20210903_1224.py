# Generated by Django 3.2.5 on 2021-09-03 12:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0026_auto_20210827_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_001',
            name='mid_ph_001',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index_001',
            name='mid_ph_002',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index_001',
            name='mid_ph_003',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index_001',
            name='mid_ph_004',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index_001',
            name='mid_ph_005',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index_001',
            name='mid_ph_006',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

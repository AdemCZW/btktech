# Generated by Django 3.2.5 on 2021-08-10 10:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0016_auto_20210810_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='pd_content',
            field=ckeditor.fields.RichTextField(max_length=1000, null=True),
        ),
    ]

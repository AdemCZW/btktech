# Generated by Django 3.2.5 on 2021-08-11 09:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0017_alter_flight_pd_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='pd_content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]

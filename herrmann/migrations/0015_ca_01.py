# Generated by Django 3.2.5 on 2022-04-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herrmann', '0014_qa_01'),
    ]

    operations = [
        migrations.CreateModel(
            name='ca_01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca_phone', models.CharField(blank=True, max_length=100000, verbose_name='電話:')),
                ('ca_mail', models.CharField(blank=True, max_length=100000, verbose_name='信箱')),
                ('ca_time', models.CharField(blank=True, max_length=100000, verbose_name='時間')),
            ],
            options={
                'verbose_name': 'contact-聯絡我們',
                'verbose_name_plural': 'contact-聯絡我們',
            },
        ),
    ]

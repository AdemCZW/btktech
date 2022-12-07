from django.db import models
from ckeditor.fields import RichTextField


class plat_home(models.Model):

    plat_phn_001 = models.CharField(
        max_length=100000, verbose_name='聯絡電話', blank=True)
    plat_adr_001 = models.CharField(
        max_length=100000, verbose_name='聯絡地址', blank=True)
    plat_mail_001 = models.CharField(
        max_length=100000, verbose_name='聯絡信箱', blank=True)

    def __str__(self):
        return "基本資訊"

    class Meta:
        verbose_name_plural = "基本資訊"
        verbose_name = "基本資訊"


class plat_index(models.Model):
    loop_ph_001 = models.CharField(
        max_length=100000, verbose_name='插入圖片', blank=True)

    def __str__(self):
        return "Home"

    class Meta:
        verbose_name_plural = "Home"
        verbose_name = "Home"

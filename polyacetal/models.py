from django.db import models
from ckeditor.fields import RichTextField


class home_poly(models.Model):

    poly_index_001 = models.CharField(
        max_length=100000, verbose_name='文字', blank=True)
    poly_index_002 = models.CharField(
        max_length=100000, verbose_name='輪播圖片-1', blank=True)
    poly_index_003 = models.CharField(
        max_length=100000, verbose_name='輪播圖片-2', blank=True)
    poly_index_004 = models.CharField(
        max_length=100000, verbose_name='輪播圖片-3', blank=True)
    poly_index_005 = models.CharField(
        max_length=100000, verbose_name='輪播圖片-4', blank=True)
    poly_index_006 = models.CharField(
        max_length=100000, verbose_name='輪播圖片-5', blank=True)

    def __str__(self):
        return " No. " + str(self.id)

    class Meta:
        verbose_name_plural = "poly-home"
        verbose_name = "poly-home"


class ffmm_page(models.Model):

    ffmm_tit = models.CharField(
        max_length=100000, verbose_name='產品標題', blank=True)
    ffmm_num = models.CharField(
        max_length=100000, verbose_name='產品型號', blank=True)
    ffmm_img = models.CharField(
        max_length=100000, verbose_name='產品圖片', blank=True)
    ffmm_det = RichTextField(
        max_length=10000, default='產品規格', blank=True, null=True, verbose_name='內容')

    def __str__(self):
        return " No. " + str(self.id)

    class Meta:
        verbose_name_plural = "file folder"
        verbose_name = "file folder"

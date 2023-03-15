from django.db import models
from ckeditor.fields import RichTextField


class home_poly(models.Model):
    poly_index_001 = models.CharField(
        max_length=1000, verbose_name='文字', blank=True)
    poly_index_002 = models.CharField(
        max_length=1000, verbose_name='輪播圖片-1', blank=True)
    poly_index_003 = models.CharField(
        max_length=1000, verbose_name='輪播圖片-2', blank=True)
    poly_index_004 = models.CharField(
        max_length=1000, verbose_name='輪播圖片-3', blank=True)
    poly_index_005 = models.CharField(
        max_length=1000, verbose_name='輪播圖片-4', blank=True)
    poly_index_006 = models.CharField(
        max_length=1000, verbose_name='輪播圖片-5', blank=True)

    def __str__(self):
        return " No. " + str(self.id)

    class Meta:
        verbose_name_plural = "poly-home"
        verbose_name = "poly-home"


class ffmm_page(models.Model):
    ffmm_tit = models.CharField(
        max_length=1000, verbose_name='產品標題', blank=True)
    ffmm_num = models.CharField(
        max_length=1000, verbose_name='產品型號', blank=True)
    ffmm_img = models.CharField(
        max_length=1000, verbose_name='產品圖片', blank=True)
    ffmm_det = RichTextField(
        max_length=10000, default='產品規格', blank=True, null=True, verbose_name='內容')

    def __str__(self):
        return " No. " + str(self.id)

    class Meta:
        verbose_name_plural = "File Folder"
        verbose_name = "File Folder"


class bcm_page(models.Model):
    bcm_tit = models.CharField(
        max_length=1000, verbose_name='產品標題', blank=True)
    bcm_num = models.CharField(
        max_length=1000, verbose_name='產品型號', blank=True)
    bcm_img = models.CharField(
        max_length=1000, verbose_name='產品圖片', blank=True)
    bcm_det = RichTextField(
        max_length=10000, default='產品規格', blank=True, null=True, verbose_name='內容')

    def __str__(self):
        return " No. " + str(self.id)

    class Meta:
        verbose_name_plural = "Bag Converting"
        verbose_name = "Bag Converting"


class bes_page(models.Model):
    bes_tit = models.CharField(
        max_length=1000, verbose_name='產品標題', blank=True)
    bes_num = models.CharField(
        max_length=1000, verbose_name='產品型號', blank=True)
    bes_img = models.CharField(
        max_length=1000, verbose_name='產品圖片', blank=True)
    bes_det = RichTextField(
        max_length=10000, default='產品規格', blank=True, null=True, verbose_name='內容')

    def __str__(self):
        return " No. " + str(self.id)

    class Meta:
        verbose_name_plural = "Bubble Envelope"
        verbose_name = "Bubble Envelope"


class el_page(models.Model):
    el_tit = models.CharField(
        max_length=1000, verbose_name='產品標題', blank=True)
    el_num = models.CharField(
        max_length=1000, verbose_name='產品型號', blank=True)
    el_img = models.CharField(
        max_length=1000, verbose_name='產品圖片', blank=True)
    el_det = RichTextField(
        max_length=10000, default='產品規格', blank=True, null=True, verbose_name='內容')

    def __str__(self):
        return " No. " + str(self.id)

    class Meta:
        verbose_name_plural = "Extrusion Line"
        verbose_name = "Extrusion Line"


class ma_page(models.Model):
    ma_tit = models.CharField(
        max_length=1000, verbose_name='產品標題', blank=True)
    ma_num = models.CharField(
        max_length=1000, verbose_name='產品型號', blank=True)
    ma_img = models.CharField(
        max_length=1000, verbose_name='產品圖片', blank=True)
    ma_det = RichTextField(
        max_length=10000, default='產品規格', blank=True, null=True, verbose_name='內容')

    def __str__(self):
        return " No. " + str(self.id)

    class Meta:
        verbose_name_plural = "Mask Application"
        verbose_name = "Mask Application"

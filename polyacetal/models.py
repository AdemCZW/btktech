from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class home_poly(models.Model):

    poly_index_001 = models.CharField(
        max_length=100000, verbose_name='文字', blank=True)

    def __str__(self):
        return "塑膠首頁"

    class Meta:
        verbose_name_plural = "塑膠首頁"
        verbose_name = "塑膠首頁"

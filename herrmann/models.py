from django.db import models
from ckeditor.fields import RichTextField

class home(models.Model):

	phn_001 = models.CharField(max_length=1000,verbose_name = '聯絡電話', blank=True )
	adr_001 = models.CharField(max_length=1000,verbose_name = '聯絡地址', blank=True )
	mail_001 = models.CharField(max_length=1000,verbose_name = '聯絡信箱', blank=True )

	def __str__(self):
		return "基本資訊"

	class Meta:
		verbose_name_plural = "基本資訊"
		verbose_name = "基本資訊"

class index_01(models.Model):
	mid_tit_001 = models.CharField(max_length=1000,verbose_name = '左上-標題', blank=True )
	mid_txt_001 = models.CharField(max_length=1000,verbose_name = '左上', blank=True )
	mid_tit_002 = models.CharField(max_length=1000,verbose_name = '中上-標題', blank=True )
	mid_txt_002 = models.CharField(max_length=1000,verbose_name = '中上', blank=True )
	mid_tit_003 = models.CharField(max_length=1000,verbose_name = '右上-標題', blank=True )
	mid_txt_003 = models.CharField(max_length=1000,verbose_name = '右上', blank=True )
	mid_tit_004 = models.CharField(max_length=1000,verbose_name = '左下-標題', blank=True )
	mid_txt_004 = models.CharField(max_length=1000,verbose_name = '左下', blank=True )
	mid_tit_005 = models.CharField(max_length=1000,verbose_name = '中下-標題', blank=True )
	mid_txt_005 = models.CharField(max_length=1000,verbose_name = '中下', blank=True )
	mid_tit_006 = models.CharField(max_length=1000,verbose_name = '右下-標題', blank=True )
	mid_txt_006 = models.CharField(max_length=1000,verbose_name = '右下', blank=True )

	def __str__(self):
		return "首頁"

	class Meta:
		verbose_name_plural = "首頁"
		verbose_name = "首頁"

class welding_01(models.Model):
	welding_tit_001 = models.CharField(max_length=1000,verbose_name = '產品特色標題-1', blank=True )
	welding_txt_001 = RichTextField(max_length=1000,verbose_name = '產品特色內容-1', blank=True )
	welding_tit_002 = models.CharField(max_length=1000,verbose_name = '產品特色標題-2', blank=True )
	welding_txt_002 = RichTextField(max_length=1000,verbose_name = '產品特色內容-2', blank=True )
	welding_tit_003 = models.CharField(max_length=1000,verbose_name = '產品特色標題-3', blank=True )
	welding_txt_003 = RichTextField(max_length=1000,verbose_name = '產品特色內容-3', blank=True )

	def __str__(self):
		return "welding-簡介"

	class Meta:
		verbose_name_plural = "welding-簡介"
		verbose_name = "welding-簡介"

class welding_02(models.Model):
	welding_tit = models.CharField(max_length=1000,verbose_name = '產品名稱', blank=True )
	welding_cont = RichTextField(max_length=1000,verbose_name = '主要產品說明', blank=True )
	welding_img_001 = models.CharField(max_length=1000,verbose_name = '產品圖片-1', blank=True )
	welding_seri_001_tit_01 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-1', blank=True )
	welding_seri_001_1 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_02 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-2', blank=True )
	welding_seri_001_2 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_03 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-3', blank=True )
	welding_seri_001_3 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_04 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-4', blank=True )
	welding_seri_001_4 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')

	def __str__(self):
		return "welding-品項" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "welding-品項"
		verbose_name = "welding-品項"

class cpn_01(models.Model):
	cpn_tit = models.CharField(max_length=1000,verbose_name = '產品名稱', blank=True )
	cpn_cont = RichTextField(max_length=1000,verbose_name = '主要產品說明', blank=True )
	cpn_img_001 = models.CharField(max_length=1000,verbose_name = '產品圖片-1', blank=True )
	cpn_seri_001_tit_01 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-1', blank=True )
	cpn_seri_001_1 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_02 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-2', blank=True )
	cpn_seri_001_2 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_03 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-3', blank=True )
	cpn_seri_001_3 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_04 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-4', blank=True )
	cpn_seri_001_4 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')

	def __str__(self):
		return "components-品項" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "components-品項"
		verbose_name = "components-品項"

class mta_01(models.Model):
	mta_tit = models.CharField(max_length=1000,verbose_name = '產品名稱', blank=True )
	mta_cont = RichTextField(max_length=1000,verbose_name = '主要產品說明', blank=True )
	mta_img_001 = models.CharField(max_length=1000,verbose_name = '產品圖片-1', blank=True )
	mta_seri_001_tit_01 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-1', blank=True )
	mta_seri_001_1 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_02 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-2', blank=True )
	mta_seri_001_2 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_03 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-3', blank=True )
	mta_seri_001_3 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_04 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-4', blank=True )
	mta_seri_001_4 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')

	def __str__(self):
		return "metal-品項" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "metal-品項"
		verbose_name = "metal-品項"

class sys_01(models.Model):
	sys_tit = models.CharField(max_length=1000,verbose_name = '產品名稱', blank=True )
	sys_cont = RichTextField(max_length=1000,verbose_name = '主要產品說明', blank=True )
	sys_img_001 = models.CharField(max_length=1000,verbose_name = '產品圖片-1', blank=True )
	sys_seri_001_tit_01 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-1', blank=True )
	sys_seri_001_1 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_02 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-2', blank=True )
	sys_seri_001_2 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_03 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-3', blank=True )
	sys_seri_001_3 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_04 = models.CharField(max_length=1000,verbose_name = '產品系列-標題-4', blank=True )
	sys_seri_001_4 = RichTextField(max_length=10000,default='文字敘述',blank=True, null=True,verbose_name = '內容')

	def __str__(self):
		return "application-應用" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "application-應用"
		verbose_name = "application-應用"



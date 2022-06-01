from django.db import models
from ckeditor.fields import RichTextField

class home(models.Model):

	phn_001 = models.CharField(max_length=100000,verbose_name = '聯絡電話', blank=True )
	adr_001 = models.CharField(max_length=100000,verbose_name = '聯絡地址', blank=True )
	mail_001 = models.CharField(max_length=100000,verbose_name = '聯絡信箱', blank=True )

	def __str__(self):
		return "基本資訊"

	class Meta:
		verbose_name_plural = "基本資訊"
		verbose_name = "基本資訊"

class index_01(models.Model):
	mid_tit_001 = models.CharField(max_length=100000,verbose_name = '左上-標題', blank=True )
	mid_txt_001 = models.CharField(max_length=100000,verbose_name = '左上', blank=True )
	mid_tit_002 = models.CharField(max_length=100000,verbose_name = '中上-標題', blank=True )
	mid_txt_002 = models.CharField(max_length=100000,verbose_name = '中上', blank=True )
	mid_tit_003 = models.CharField(max_length=100000,verbose_name = '右上-標題', blank=True )
	mid_txt_003 = models.CharField(max_length=100000,verbose_name = '右上', blank=True )
	mid_tit_004 = models.CharField(max_length=100000,verbose_name = '左下-標題', blank=True )
	mid_txt_004 = models.CharField(max_length=100000,verbose_name = '左下', blank=True )
	mid_tit_005 = models.CharField(max_length=100000,verbose_name = '中下-標題', blank=True )
	mid_txt_005 = models.CharField(max_length=100000,verbose_name = '中下', blank=True )
	mid_tit_006 = models.CharField(max_length=100000,verbose_name = '右下-標題', blank=True )
	mid_txt_006 = models.CharField(max_length=100000,verbose_name = '右下', blank=True )

	mid_tit_007 = models.CharField(max_length=100000,verbose_name = 'EN-左上-標題', blank=True )
	mid_txt_007 = models.CharField(max_length=100000,verbose_name = 'EN-左上', blank=True )
	mid_tit_008 = models.CharField(max_length=100000,verbose_name = 'EN-中上-標題', blank=True )
	mid_txt_008 = models.CharField(max_length=100000,verbose_name = 'EN-中上', blank=True )
	mid_tit_009 = models.CharField(max_length=100000,verbose_name = 'EN-右上-標題', blank=True )
	mid_txt_009 = models.CharField(max_length=100000,verbose_name = 'EN-右上', blank=True )
	mid_tit_010 = models.CharField(max_length=100000,verbose_name = 'EN-左下-標題', blank=True )
	mid_txt_010 = models.CharField(max_length=100000,verbose_name = 'EN-左下', blank=True )
	mid_tit_011 = models.CharField(max_length=100000,verbose_name = 'EN-中下-標題', blank=True )
	mid_txt_011 = models.CharField(max_length=100000,verbose_name = 'EN-中下', blank=True )
	mid_tit_012 = models.CharField(max_length=100000,verbose_name = 'EN-右下-標題', blank=True )
	mid_txt_012 = models.CharField(max_length=100000,verbose_name = 'EN-右下', blank=True )

	mid_tit_013 = models.CharField(max_length=100000,verbose_name = 'SP-左上-標題', blank=True )
	mid_txt_013 = models.CharField(max_length=100000,verbose_name = 'SP-左上', blank=True )
	mid_tit_014 = models.CharField(max_length=100000,verbose_name = 'SP-中上-標題', blank=True )
	mid_txt_014 = models.CharField(max_length=100000,verbose_name = 'SP-中上', blank=True )
	mid_tit_015 = models.CharField(max_length=100000,verbose_name = 'SP-右上-標題', blank=True )
	mid_txt_015 = models.CharField(max_length=100000,verbose_name = 'SP-右上', blank=True )
	mid_tit_016 = models.CharField(max_length=100000,verbose_name = 'SP-左下-標題', blank=True )
	mid_txt_016 = models.CharField(max_length=100000,verbose_name = 'SP-左下', blank=True )
	mid_tit_017 = models.CharField(max_length=100000,verbose_name = 'SP-中下-標題', blank=True )
	mid_txt_017 = models.CharField(max_length=100000,verbose_name = 'SP-中下', blank=True )
	mid_tit_018 = models.CharField(max_length=100000,verbose_name = 'SP-右下-標題', blank=True )
	mid_txt_018 = models.CharField(max_length=100000,verbose_name = 'SP-右下', blank=True )

	def __str__(self):
		return "Home"

	class Meta:
		verbose_name_plural = "Home"
		verbose_name = "Home"

class welding_01(models.Model):
	welding_tit_001 = models.CharField(max_length=100000,verbose_name = '產品特色標題-1', blank=True )
	welding_txt_001 = RichTextField(max_length=100000,verbose_name = '產品特色內容-1', blank=True )
	welding_tit_002 = models.CharField(max_length=100000,verbose_name = '產品特色標題-2', blank=True )
	welding_txt_002 = RichTextField(max_length=100000,verbose_name = '產品特色內容-2', blank=True )
	welding_tit_003 = models.CharField(max_length=100000,verbose_name = '產品特色標題-3', blank=True )
	welding_txt_003 = RichTextField(max_length=100000,verbose_name = '產品特色內容-3', blank=True )

	def __str__(self):
		return "welding-簡介"

	class Meta:
		verbose_name_plural = "welding-簡介"
		verbose_name = "welding-簡介"

class welding_02(models.Model):
	welding_tit = models.CharField(max_length=100000,verbose_name = '產品名稱', blank=True )
	welding_cont = RichTextField(max_length=100000,verbose_name = '主要產品說明', blank=True )
	welding_img_001 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	welding_seri_001_tit_01 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-1', blank=True )
	welding_seri_001_1 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_02 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-2', blank=True )
	welding_seri_001_2 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_03 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-3', blank=True )
	welding_seri_001_3 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_04 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-4', blank=True )
	welding_seri_001_4 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')

	welding_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-產品名稱', blank=True )
	welding_cont_en = RichTextField(max_length=100000,verbose_name = 'EN-主要產品說明', blank=True )
	welding_img_001_en = models.CharField(max_length=100000,verbose_name = 'EN-產品圖片-1', blank=True )
	welding_seri_001_tit_01_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-1', blank=True )
	welding_seri_001_1_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_02_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-2', blank=True )
	welding_seri_001_2_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_03_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-3', blank=True )
	welding_seri_001_3_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_04_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-4', blank=True )
	welding_seri_001_4_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	
	welding_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品名稱', blank=True )
	welding_cont_sp = RichTextField(max_length=100000,verbose_name = 'SP-主要產品說明', blank=True )
	welding_img_001_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品圖片-1', blank=True )
	welding_seri_001_tit_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-1', blank=True )
	welding_seri_001_1_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-2', blank=True )
	welding_seri_001_2_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-3', blank=True )
	welding_seri_001_3_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	welding_seri_001_tit_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-4', blank=True )
	welding_seri_001_4_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	
	def __str__(self):
		return "welding" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "Ultrasonic Welding Machine"
		verbose_name = "Ultrasonic Welding Machine"
		ordering = ['id']

class cpn_01(models.Model):
	cpn_tit = models.CharField(max_length=100000,verbose_name = '產品名稱', blank=True )
	cpn_cont = RichTextField(max_length=100000,verbose_name = '主要產品說明', blank=True )
	cpn_img_001 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	cpn_seri_001_tit_01 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-1', blank=True )
	cpn_seri_001_1 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_02 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-2', blank=True )
	cpn_seri_001_2 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_03 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-3', blank=True )
	cpn_seri_001_3 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_04 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-4', blank=True )
	cpn_seri_001_4 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')

	cpn_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-EN-產品名稱', blank=True )
	cpn_cont_en = RichTextField(max_length=100000,verbose_name = 'EN-主要產品說明', blank=True )
	cpn_img_001_en = models.CharField(max_length=100000,verbose_name = 'EN-產品圖片-1', blank=True )
	cpn_seri_001_tit_01_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-1', blank=True )
	cpn_seri_001_1_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_02_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-2', blank=True )
	cpn_seri_001_2_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_03_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-3', blank=True )
	cpn_seri_001_3_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_04_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-4', blank=True )
	cpn_seri_001_4_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	
	cpn_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-SP-產品名稱', blank=True )
	cpn_cont_sp = RichTextField(max_length=100000,verbose_name = 'SP-主要產品說明', blank=True )
	cpn_img_001_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品圖片-1', blank=True )
	cpn_seri_001_tit_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-1', blank=True )
	cpn_seri_001_1_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-2', blank=True )
	cpn_seri_001_2_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-3', blank=True )
	cpn_seri_001_3_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	cpn_seri_001_tit_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-4', blank=True )
	cpn_seri_001_4_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	
	def __str__(self):
		return "components" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "Ultrasonic Components"
		verbose_name = "Ultrasonic Components"
		ordering = ['id']

class mta_01(models.Model):
	mta_tit = models.CharField(max_length=100000,verbose_name = '產品名稱', blank=True )
	mta_cont = RichTextField(max_length=100000,verbose_name = '主要產品說明', blank=True )
	mta_img_001 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	mta_seri_001_tit_01 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-1', blank=True )
	mta_seri_001_1 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_02 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-2', blank=True )
	mta_seri_001_2 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_03 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-3', blank=True )
	mta_seri_001_3 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_04 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-4', blank=True )
	mta_seri_001_4 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')

	mta_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-產品名稱', blank=True )
	mta_cont_en = RichTextField(max_length=100000,verbose_name = 'EN-主要產品說明', blank=True )
	mta_img_001_en = models.CharField(max_length=100000,verbose_name = 'EN-產品圖片-1', blank=True )
	mta_seri_001_tit_01_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-1', blank=True )
	mta_seri_001_1_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_02_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-2', blank=True )
	mta_seri_001_2_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_03_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-3', blank=True )
	mta_seri_001_3_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_04_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-4', blank=True )
	mta_seri_001_4_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')

	mta_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品名稱', blank=True )
	mta_cont_sp = RichTextField(max_length=100000,verbose_name = 'SP-主要產品說明', blank=True )
	mta_img_001_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品圖片-1', blank=True )
	mta_seri_001_tit_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-1', blank=True )
	mta_seri_001_1_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-2', blank=True )
	mta_seri_001_2_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-3', blank=True )
	mta_seri_001_3_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	mta_seri_001_tit_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-4', blank=True )
	mta_seri_001_4_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')

	def __str__(self):
		return "metal" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "Ultrasonic Welding Metal"
		verbose_name = "Ultrasonic Welding Metal"
		ordering = ['id']

class sys_01(models.Model):
	sys_tit = models.CharField(max_length=100000,verbose_name = '產品名稱', blank=True )
	sys_cont = RichTextField(max_length=100000,verbose_name = '主要產品說明', blank=True )
	sys_img_001 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	sys_seri_001_tit_01 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-1', blank=True )
	sys_seri_001_1 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_02 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-2', blank=True )
	sys_seri_001_2 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_03 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-3', blank=True )
	sys_seri_001_3 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_04 = models.CharField(max_length=100000,verbose_name = '產品系列-標題-4', blank=True )
	sys_seri_001_4 = RichTextField(max_length=1000000,default='文字敘述',blank=True, null=True,verbose_name = '內容')

	sys_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-產品名稱', blank=True )
	sys_cont_en = RichTextField(max_length=100000,verbose_name = 'EN-主要產品說明', blank=True )
	sys_img_001_en = models.CharField(max_length=100000,verbose_name = 'EN-產品圖片-1', blank=True )
	sys_seri_001_tit_01_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-1', blank=True )
	sys_seri_001_1_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_02_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-2', blank=True )
	sys_seri_001_2_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_03_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-3', blank=True )
	sys_seri_001_3_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_04_en = models.CharField(max_length=100000,verbose_name = 'EN-產品系列-標題-4', blank=True )
	sys_seri_001_4_en = RichTextField(max_length=1000000,default='EN-文字敘述',blank=True, null=True,verbose_name = '內容')

	sys_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品名稱', blank=True )
	sys_cont_sp = RichTextField(max_length=100000,verbose_name = 'SP-主要產品說明', blank=True )
	sys_img_001_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品圖片-1', blank=True )
	sys_seri_001_tit_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-1', blank=True )
	sys_seri_001_1_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-2', blank=True )
	sys_seri_001_2_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-3', blank=True )
	sys_seri_001_3_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')
	sys_seri_001_tit_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-產品系列-標題-4', blank=True )
	sys_seri_001_4_sp = RichTextField(max_length=1000000,default='SP-文字敘述',blank=True, null=True,verbose_name = '內容')


	def __str__(self):
		return "system" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "Ultrasonic Welding system"
		verbose_name = "Ultrasonic Welding system"
		ordering = ['id']

class qa_01(models.Model):
	qa_tit = models.CharField(max_length=100000,verbose_name = 'Ｑ:', blank=True )
	qa_cont = RichTextField(max_length=100000,verbose_name = 'A:', blank=True )
	
	def __str__(self):
		return "QA" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "QA"
		verbose_name = "QA"
		ordering = ['id']

class ca_01(models.Model):
	ca_phone = models.CharField(max_length=100000,verbose_name = '電話:', blank=True )
	ca_mail = models.CharField(max_length=100000,verbose_name = '信箱', blank=True )
	ca_time = models.CharField(max_length=100000,verbose_name = '時間', blank=True )
	
	def __str__(self):
		return "contact-聯絡我們" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "contact-聯絡我們"
		verbose_name = "contact-聯絡我們"

class food_01(models.Model):
	food_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	food_ctn = RichTextField(max_length=100000,verbose_name = '內容', blank=True )
	food_pho_01 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	food_pho_02 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	food_pho_03 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	food_pho_04 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	food_pho_05 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	food_pho_06 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	food_pho_07 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	food_pho_08 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )

	food_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-標題', blank=True )
	food_ctn_en = RichTextField(max_length=100000,verbose_name = 'EN-內容', blank=True )
	food_pho_01_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	food_pho_02_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	food_pho_03_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	food_pho_04_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	food_pho_05_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	food_pho_06_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	food_pho_07_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	food_pho_08_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )

	food_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-標題', blank=True )
	food_ctn_sp = RichTextField(max_length=100000,verbose_name = 'SP-內容', blank=True )
	food_pho_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	food_pho_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	food_pho_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	food_pho_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	food_pho_05_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	food_pho_06_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	food_pho_07_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	food_pho_08_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	
	
	def __str__(self):
		return "Food" + str(self.id) 

	class Meta:
		verbose_name_plural = "Branch-Food"
		verbose_name = "Branch-Food"

class automation_01(models.Model):
	automation_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	automation_ctn = RichTextField(max_length=100000,verbose_name = '內容', blank=True )
	automation_pho_01 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automation_pho_02 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automation_pho_03 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automation_pho_04 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automation_pho_05 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automation_pho_06 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automation_pho_07 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automation_pho_08 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	automation_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-標題', blank=True )
	automation_ctn_en = RichTextField(max_length=100000,verbose_name = 'EN-內容', blank=True )
	automation_pho_01_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automation_pho_02_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automation_pho_03_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automation_pho_04_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automation_pho_05_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automation_pho_06_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automation_pho_07_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automation_pho_08_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )

	automation_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-標題', blank=True )
	automation_ctn_sp = RichTextField(max_length=100000,verbose_name = 'SP-內容', blank=True )
	automation_pho_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automation_pho_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automation_pho_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automation_pho_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automation_pho_05_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automation_pho_06_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automation_pho_07_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automation_pho_08_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	
	def __str__(self):
		return "automation" + str(self.id) 

	class Meta:
		verbose_name_plural = "Branch-Automation"
		verbose_name = "Branch-Automation"

class automotive_01(models.Model):
	automotive_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	automotive_ctn = RichTextField(max_length=100000,verbose_name = '內容', blank=True )
	automotive_pho_01 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automotive_pho_02 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automotive_pho_03 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automotive_pho_04 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automotive_pho_05 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automotive_pho_06 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automotive_pho_07 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	automotive_pho_08 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	automotive_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-標題', blank=True )
	automotive_ctn_en = RichTextField(max_length=100000,verbose_name = 'EN-內容', blank=True )
	automotive_pho_01_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automotive_pho_02_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automotive_pho_03_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automotive_pho_04_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automotive_pho_05_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automotive_pho_06_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automotive_pho_07_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	automotive_pho_08_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )

	automotive_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-標題', blank=True )
	automotive_ctn_sp = RichTextField(max_length=100000,verbose_name = 'SP-內容', blank=True )
	automotive_pho_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automotive_pho_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automotive_pho_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automotive_pho_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automotive_pho_05_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automotive_pho_06_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automotive_pho_07_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	automotive_pho_08_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	
	def __str__(self):
		return "automotive" + str(self.id) 

	class Meta:
		verbose_name_plural = "Branch-Automotive"
		verbose_name = "Branch-Automotive"

class hygiene_01(models.Model):
	hygiene_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	hygiene_ctn = RichTextField(max_length=100000,verbose_name = '內容', blank=True )
	hygiene_pho_01 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	hygiene_pho_02 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	hygiene_pho_03 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	hygiene_pho_04 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	hygiene_pho_05 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	hygiene_pho_06 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	hygiene_pho_07 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	hygiene_pho_08 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )

	hygiene_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-標題', blank=True )
	hygiene_ctn_en = RichTextField(max_length=100000,verbose_name = 'EN-內容', blank=True )
	hygiene_pho_01_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	hygiene_pho_02_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	hygiene_pho_03_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	hygiene_pho_04_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	hygiene_pho_05_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	hygiene_pho_06_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	hygiene_pho_07_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	hygiene_pho_08_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )

	hygiene_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-標題', blank=True )
	hygiene_ctn_sp = RichTextField(max_length=100000,verbose_name = 'SP-內容', blank=True )
	hygiene_pho_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	hygiene_pho_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	hygiene_pho_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	hygiene_pho_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	hygiene_pho_05_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	hygiene_pho_06_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	hygiene_pho_07_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	hygiene_pho_08_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	
	def __str__(self):
		return "hygiene" + str(self.id) 

	class Meta:
		verbose_name_plural = "Branch-Hygiene"
		verbose_name = "Branch-Hygiene"

class medical_01(models.Model):
	medical_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	medical_ctn = RichTextField(max_length=100000,verbose_name = '內容', blank=True )
	medical_pho_01 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	medical_pho_02 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	medical_pho_03 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	medical_pho_04 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	medical_pho_05 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	medical_pho_06 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	medical_pho_07 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	medical_pho_08 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	medical_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-標題', blank=True )
	medical_ctn_en = RichTextField(max_length=100000,verbose_name = 'EN-內容', blank=True )
	medical_pho_01_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	medical_pho_02_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	medical_pho_03_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	medical_pho_04_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	medical_pho_05_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	medical_pho_06_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	medical_pho_07_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	medical_pho_08_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )

	medical_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-標題', blank=True )
	medical_ctn_sp = RichTextField(max_length=100000,verbose_name = 'SP-內容', blank=True )
	medical_pho_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	medical_pho_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	medical_pho_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	medical_pho_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	medical_pho_05_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	medical_pho_06_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	medical_pho_07_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	medical_pho_08_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	
	def __str__(self):
		return "medical" + str(self.id) 

	class Meta:
		verbose_name_plural = "Branch-Medical"
		verbose_name = "Branch-Medical"

class electronics_01(models.Model):
	electronics_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	electronics_ctn = RichTextField(max_length=100000,verbose_name = '內容', blank=True )
	electronics_pho_01 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	electronics_pho_02 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	electronics_pho_03 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	electronics_pho_04 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	electronics_pho_05 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	electronics_pho_06 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	electronics_pho_07 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	electronics_pho_08 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )

	electronics_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-標題', blank=True )
	electronics_ctn_en = RichTextField(max_length=100000,verbose_name = 'EN-內容', blank=True )
	electronics_pho_01_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	electronics_pho_02_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	electronics_pho_03_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	electronics_pho_04_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	electronics_pho_05_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	electronics_pho_06_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	electronics_pho_07_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	electronics_pho_08_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )

	electronics_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-標題', blank=True )
	electronics_ctn_sp = RichTextField(max_length=100000,verbose_name = 'SP-內容', blank=True )
	electronics_pho_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	electronics_pho_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	electronics_pho_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	electronics_pho_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	electronics_pho_05_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	electronics_pho_06_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	electronics_pho_07_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	electronics_pho_08_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	
	def __str__(self):
		return "electronics" + str(self.id) 

	class Meta:
		verbose_name_plural = "Branch-Electronics"
		verbose_name = "Branch-Electronics"

class battery_01(models.Model):
	battery_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	battery_ctn = RichTextField(max_length=100000,verbose_name = '內容', blank=True )
	battery_pho_01 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	battery_pho_02 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	battery_pho_03 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	battery_pho_04 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	battery_pho_05 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	battery_pho_06 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	battery_pho_07 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	battery_pho_08 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )

	battery_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-標題', blank=True )
	battery_ctn_en = RichTextField(max_length=100000,verbose_name = 'EN-內容', blank=True )
	battery_pho_01_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	battery_pho_02_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	battery_pho_03_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	battery_pho_04_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	battery_pho_05_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	battery_pho_06_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	battery_pho_07_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	battery_pho_08_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )

	battery_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-標題', blank=True )
	battery_ctn_sp = RichTextField(max_length=100000,verbose_name = 'SP-內容', blank=True )
	battery_pho_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	battery_pho_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	battery_pho_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	battery_pho_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	battery_pho_05_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	battery_pho_06_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	battery_pho_07_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	battery_pho_08_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	
	def __str__(self):
		return "battery" + str(self.id) 

	class Meta:
		verbose_name_plural = "Branch-Battery"
		verbose_name = "Branch-Battery"

class consumer_01(models.Model):
	consumer_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	consumer_ctn = RichTextField(max_length=100000,verbose_name = '內容', blank=True )
	consumer_pho_01 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	consumer_pho_02 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	consumer_pho_03 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	consumer_pho_04 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	consumer_pho_05 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	consumer_pho_06 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	consumer_pho_07 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	consumer_pho_08 = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )

	consumer_tit_en = models.CharField(max_length=100000,verbose_name = 'EN-標題', blank=True )
	consumer_ctn_en = RichTextField(max_length=100000,verbose_name = 'EN-內容', blank=True )
	consumer_pho_01_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	consumer_pho_02_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	consumer_pho_03_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	consumer_pho_04_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	consumer_pho_05_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	consumer_pho_06_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	consumer_pho_07_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )
	consumer_pho_08_en = models.CharField(max_length=100000,verbose_name = 'EN-圖片', blank=True )

	consumer_tit_sp = models.CharField(max_length=100000,verbose_name = 'SP-標題', blank=True )
	consumer_ctn_sp = RichTextField(max_length=100000,verbose_name = 'SP-內容', blank=True )
	consumer_pho_01_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	consumer_pho_02_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	consumer_pho_03_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	consumer_pho_04_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	consumer_pho_05_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	consumer_pho_06_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	consumer_pho_07_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	consumer_pho_08_sp = models.CharField(max_length=100000,verbose_name = 'SP-圖片', blank=True )
	
	def __str__(self):
		return "consumer" + str(self.id) 

	class Meta:
		verbose_name_plural = "Branch-Consumer"
		verbose_name = "Branch-Consumer"


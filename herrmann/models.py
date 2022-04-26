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

	def __str__(self):
		return "首頁"

	class Meta:
		verbose_name_plural = "首頁"
		verbose_name = "首頁"

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

	def __str__(self):
		return "welding-品項" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "welding-品項"
		verbose_name = "welding-品項"
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

	def __str__(self):
		return "components-品項" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "components-品項"
		verbose_name = "components-品項"
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

	def __str__(self):
		return "對應超音波金屬熔接" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "對應超音波金屬熔接"
		verbose_name = "對應超音波金屬熔接"
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

	def __str__(self):
		return "對應超音波集成系統" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "對應超音波集成系統"
		verbose_name = "對應超音波集成系統"
		ordering = ['id']

class bc_01(models.Model):
	bc_tit = models.CharField(max_length=100000,verbose_name = '產品名稱', blank=True )
	bc_cont = RichTextField(max_length=100000,verbose_name = '主要產品說明', blank=True )
	bc_img_001 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_002 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_003 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_004 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_005 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_006 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_007 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_008 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_009 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	bc_img_010 = models.CharField(max_length=100000,verbose_name = '產品圖片-1', blank=True )
	
	
	def __str__(self):
		return "Branches-超音波應用" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "Branches-超音波應用"
		verbose_name = "Branches-超音波應用"
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
	
	def __str__(self):
		return "Food" + str(self.id) 

	class Meta:
		verbose_name_plural = "Food"
		verbose_name = "Food"

class automation_01(models.Model):
	automation_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	automation_ctn = models.CharField(max_length=100000,verbose_name = '內容', blank=True )
	automation_pho = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	def __str__(self):
		return "automation" + str(self.id) 

	class Meta:
		verbose_name_plural = "automation"
		verbose_name = "automation"

class automotive_01(models.Model):
	automotive_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	automotive_ctn = models.CharField(max_length=100000,verbose_name = '內容', blank=True )
	automotive_pho = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	def __str__(self):
		return "automotive" + str(self.id) 

	class Meta:
		verbose_name_plural = "automotive"
		verbose_name = "automotive"

class hygiene_01(models.Model):
	hygiene_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	hygiene_ctn = models.CharField(max_length=100000,verbose_name = '內容', blank=True )
	hygiene_pho = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	def __str__(self):
		return "hygiene" + str(self.id) 

	class Meta:
		verbose_name_plural = "hygiene"
		verbose_name = "hygiene"

class medical_01(models.Model):
	medical_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	medical_ctn = models.CharField(max_length=100000,verbose_name = '內容', blank=True )
	medical_pho = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	def __str__(self):
		return "medical" + str(self.id) 

	class Meta:
		verbose_name_plural = "medical"
		verbose_name = "medical"

class electronics_01(models.Model):
	electronics_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	electronics_ctn = models.CharField(max_length=100000,verbose_name = '內容', blank=True )
	electronics_pho = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	def __str__(self):
		return "electronics" + str(self.id) 

	class Meta:
		verbose_name_plural = "electronics"
		verbose_name = "electronics"

class battery_01(models.Model):
	battery_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	battery_ctn = models.CharField(max_length=100000,verbose_name = '內容', blank=True )
	battery_pho = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	def __str__(self):
		return "battery" + str(self.id) 

	class Meta:
		verbose_name_plural = "battery"
		verbose_name = "battery"

class consumer_01(models.Model):
	consumer_tit = models.CharField(max_length=100000,verbose_name = '標題', blank=True )
	consumer_ctn = models.CharField(max_length=100000,verbose_name = '內容', blank=True )
	consumer_pho = models.CharField(max_length=100000,verbose_name = '圖片', blank=True )
	
	def __str__(self):
		return "consumer" + str(self.id) 

	class Meta:
		verbose_name_plural = "consumer"
		verbose_name = "consumer"


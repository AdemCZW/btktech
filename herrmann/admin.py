from django.contrib import admin
from .models import index_01 ,welding_02 ,home ,cpn_01 ,mta_01 ,sys_01 ,qa_01 ,ca_01, food_01, automation_01, automotive_01, hygiene_01, medical_01, electronics_01, battery_01, consumer_01


class home_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(home)	

class index_01_Admin(admin.ModelAdmin):
	
	fieldsets = (
		['CH-Area', {
            'fields': ('mid_tit_001', 'mid_txt_001','mid_tit_002', 'mid_txt_002','mid_tit_003', 'mid_txt_003','mid_tit_004', 'mid_txt_004','mid_tit_005', 'mid_txt_005','mid_tit_006', 'mid_txt_006'),
        }],
        ['EN-Area', {
            'fields': ('mid_tit_007', 'mid_txt_007','mid_tit_008', 'mid_txt_008','mid_tit_009', 'mid_txt_009','mid_tit_010', 'mid_txt_010','mid_tit_011', 'mid_txt_011','mid_tit_012', 'mid_txt_012'),
        }]
    )

admin.site.register(index_01, index_01_Admin)	

class welding_02_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('welding_tit', 'welding_cont','welding_img_001', 'welding_seri_001_tit_01','welding_seri_001_1', 'welding_seri_001_tit_02','welding_seri_001_2', 'welding_seri_001_tit_03','welding_seri_001_3', 'welding_seri_001_tit_04','welding_seri_001_4'),
        }],
        ['EN-Area', {
            'fields': ('welding_tit_en', 'welding_cont_en','welding_img_001_en', 'welding_seri_001_tit_01_en','welding_seri_001_1_en', 'welding_seri_001_tit_02_en','welding_seri_001_2_en', 'welding_seri_001_tit_03_en','welding_seri_001_3_en', 'welding_seri_001_tit_04_en','welding_seri_001_4_en'),
        }]
    )

admin.site.register(welding_02, welding_02_Admin)	
# Register your models here.

class cpn_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('cpn_tit', 'cpn_cont','cpn_img_001', 'cpn_seri_001_tit_01','cpn_seri_001_1', 'cpn_seri_001_tit_02','cpn_seri_001_2', 'cpn_seri_001_tit_03','cpn_seri_001_3', 'cpn_seri_001_tit_04','cpn_seri_001_4'),
        }],
        ['EN-Area', {
            'fields': ('cpn_tit_en', 'cpn_cont_en','cpn_img_001_en', 'cpn_seri_001_tit_01_en','cpn_seri_001_1_en', 'cpn_seri_001_tit_02_en','cpn_seri_001_2_en', 'cpn_seri_001_tit_03_en','cpn_seri_001_3_en', 'cpn_seri_001_tit_04_en','cpn_seri_001_4_en'),
        }]
    )

admin.site.register(cpn_01, cpn_01_Admin)	
# Register your models here.
class mta_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('mta_tit', 'mta_cont','mta_img_001', 'mta_seri_001_tit_01','mta_seri_001_1', 'mta_seri_001_tit_02','mta_seri_001_2', 'mta_seri_001_tit_03','mta_seri_001_3', 'mta_seri_001_tit_04','mta_seri_001_4'),
        }],
        ['EN-Area', {
            'fields': ('mta_tit_en', 'mta_cont_en','mta_img_001_en', 'mta_seri_001_tit_01_en','mta_seri_001_1_en', 'mta_seri_001_tit_02_en','mta_seri_001_2_en', 'mta_seri_001_tit_03_en','mta_seri_001_3_en', 'mta_seri_001_tit_04_en','mta_seri_001_4_en'),
        }]
    )

admin.site.register(mta_01, mta_01_Admin)	

# Register your models here.

class sys_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('sys_tit', 'sys_cont','sys_img_001', 'sys_seri_001_tit_01','sys_seri_001_1', 'sys_seri_001_tit_02','sys_seri_001_2', 'sys_seri_001_tit_03','sys_seri_001_3', 'sys_seri_001_tit_04','sys_seri_001_4'),
        }],
        ['EN-Area', {
            'fields': ('sys_tit_en', 'sys_cont_en','sys_img_001_en', 'sys_seri_001_tit_01_en','sys_seri_001_1_en', 'sys_seri_001_tit_02_en','sys_seri_001_2_en', 'sys_seri_001_tit_03_en','sys_seri_001_3_en', 'sys_seri_001_tit_04_en','sys_seri_001_4_en'),
        }]
    )

admin.site.register(sys_01, sys_01_Admin)	
# Register your models here.

class qa_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(qa_01)	
# Register your models here.

class ca_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(ca_01)	
# Register your models here.
class food_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('food_tit', 'food_ctn'),
        }],
        ['EN-Area', {
            'fields': ('food_tit_en', 'food_ctn_en'),
        }],
        ['Photo', {
        	'fields': ('food_pho_01','food_pho_02','food_pho_03','food_pho_04','food_pho_05','food_pho_06','food_pho_07','food_pho_08' )
        }]
    )

admin.site.register(food_01, food_01_Admin)	

# Register your models here.
class automation_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('automation_tit', 'automation_ctn'),
        }],
        ['EN-Area', {
            'fields': ('automation_tit_en', 'automation_ctn_en'),
        }],
        ['Photo', {
        	'fields': ('automation_pho_01','automation_pho_02','automation_pho_03','automation_pho_04','automation_pho_05','automation_pho_06','automation_pho_07','automation_pho_08' )
        }]
    )

admin.site.register(automation_01, automation_01_Admin)	
# Register your models here.

class automotive_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('automotive_tit', 'automotive_ctn'),
        }],
        ['EN-Area', {
            'fields': ('automotive_tit_en', 'automotive_ctn_en'),
        }],
        ['Photo', {
        	'fields': ('automotive_pho_01','automotive_pho_02','automotive_pho_03','automotive_pho_04','automotive_pho_05','automotive_pho_06','automotive_pho_07','automotive_pho_08' )
        }]
    )

admin.site.register(automotive_01, automotive_01_Admin)	
# Register your models here.

class hygiene_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('hygiene_tit', 'hygiene_ctn'),
        }],
        ['EN-Area', {
            'fields': ('hygiene_tit_en', 'hygiene_ctn_en'),
        }],
        ['Photo', {
        	'fields': ('hygiene_pho_01','hygiene_pho_02','hygiene_pho_03','hygiene_pho_04','hygiene_pho_05','hygiene_pho_06','hygiene_pho_07','hygiene_pho_08' )
        }]
    )

admin.site.register(hygiene_01,hygiene_01_Admin)	
# Register your models here.

class medical_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('medical_tit', 'medical_ctn'),
        }],
        ['EN-Area', {
            'fields': ('medical_tit_en', 'medical_ctn_en'),
        }],
        ['Photo', {
        	'fields': ('medical_pho_01','medical_pho_02','medical_pho_03','medical_pho_04','medical_pho_05','medical_pho_06','medical_pho_07','medical_pho_08' )
        }]
    )

admin.site.register(medical_01,medical_01_Admin)	
# Register your models here.

class electronics_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('electronics_tit', 'electronics_ctn'),
        }],
        ['EN-Area', {
            'fields': ('electronics_tit_en', 'electronics_ctn_en'),
        }],
        ['Photo', {
        	'fields': ('electronics_pho_01','electronics_pho_02','electronics_pho_03','electronics_pho_04','electronics_pho_05','electronics_pho_06','electronics_pho_07','electronics_pho_08' )
        }]
    )

admin.site.register(electronics_01,electronics_01_Admin)	
# Register your models here.

class battery_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('battery_tit', 'battery_ctn'),
        }],
        ['EN-Area', {
            'fields': ('battery_tit_en', 'battery_ctn_en'),
        }],
        ['Photo', {
        	'fields': ('battery_pho_01','battery_pho_02','battery_pho_03','battery_pho_04','battery_pho_05','battery_pho_06','battery_pho_07','battery_pho_08' )
        }]
    )
admin.site.register(battery_01, battery_01_Admin)	
# Register your models here.

class consumer_01_Admin(admin.ModelAdmin):
	fieldsets = (
		['CH-Area', {
            'fields': ('consumer_tit', 'consumer_ctn'),
        }],
        ['EN-Area', {
            'fields': ('consumer_tit_en', 'consumer_ctn_en'),
        }],
        ['Photo', {
        	'fields': ('consumer_pho_01','consumer_pho_02','consumer_pho_03','consumer_pho_04','consumer_pho_05','consumer_pho_06','consumer_pho_07','consumer_pho_08' )
        }]
    )

admin.site.register(consumer_01,consumer_01_Admin)	
# Register your models here.




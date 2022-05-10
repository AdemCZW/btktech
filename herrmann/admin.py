from django.contrib import admin
from .models import index_01 ,welding_02 ,home ,cpn_01 ,mta_01 ,sys_01 ,bc_01 ,qa_01 ,ca_01, food_01, automation_01, automotive_01, hygiene_01, medical_01, electronics_01, battery_01, consumer_01


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
	list_display = ()

admin.site.register(welding_02)	
# Register your models here.

class cpn_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(cpn_01)	
# Register your models here.

class mta_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(mta_01)	
# Register your models here.

class sys_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(sys_01)	
# Register your models here.

class bc_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(bc_01)	
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
	list_display = ()

admin.site.register(food_01)	
# Register your models here.

class automation_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(automation_01)	
# Register your models here.

class automotive_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(automotive_01)	
# Register your models here.

class hygiene_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(hygiene_01)	
# Register your models here.

class medical_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(medical_01)	
# Register your models here.

class electronics_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(electronics_01)	
# Register your models here.

class battery_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(battery_01)	
# Register your models here.

class consumer_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(consumer_01)	
# Register your models here.




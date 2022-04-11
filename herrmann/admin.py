from django.contrib import admin
from .models import index_01 ,welding_02 ,home ,cpn_01 ,mta_01 ,sys_01 ,bc_01 ,qa_01 ,ca_01


class home_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(home)	

class index_01_Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(index_01)	

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




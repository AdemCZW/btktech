from django.contrib import admin
from .models import index_01 ,welding_02 ,home ,cpn_01 ,mta_01 ,sys_01


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




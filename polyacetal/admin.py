from django.contrib import admin
from .models import home_poly, ffmm_page


class ffmm_page_Admin(admin.ModelAdmin):

    fieldsets = (
        ['CH-Area', {
            'fields': ('ffmm_tit', 'ffmm_num', 'ffmm_img', 'ffmm_det')
        }]
    )


admin.site.register(ffmm_page)
# Register your models here.

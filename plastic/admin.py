from django.contrib import admin
from .models import plat_home, plat_index


class plat_home_01(admin.ModelAdmin):

    fieldsets = (
        ['CH-Area', {
            'fields': ('plat_phn_001', 'plat_adr_001', 'plat_mail_001',)
        }],

    )


admin.site.register(plat_home, plat_home_01)


class plat_index_02(admin.ModelAdmin):

    fieldsets = (
        ['CH-Area', {
            'fields': ('loop_ph_001',)
        }],
    )


admin.site.register(plat_index, plat_index_02)

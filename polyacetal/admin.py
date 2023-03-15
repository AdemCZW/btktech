from django.contrib import admin
from .models import home_poly, ffmm_page, bcm_page, bes_page, el_page, ma_page


class home_poly_Admin(admin.ModelAdmin):

    list_display = ()


admin.site.register(home_poly)


class ffmm_page_Admin(admin.ModelAdmin):

    list_display = ()


admin.site.register(ffmm_page)


class bcm_page_Admin(admin.ModelAdmin):

    list_display = ()


admin.site.register(bcm_page)


class bes_page_Admin(admin.ModelAdmin):

    list_display = ()


admin.site.register(bes_page)


class el_page_Admin(admin.ModelAdmin):

    list_display = ()


admin.site.register(el_page)


class ma_page_Admin(admin.ModelAdmin):

    list_display = ()


admin.site.register(ma_page)

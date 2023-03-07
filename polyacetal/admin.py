from django.contrib import admin
from .models import home_poly, ffmm_page


class ffmm_page_Admin(admin.ModelAdmin):

    list_display = ()


admin.site.register(ffmm_page)
# Register your models here.

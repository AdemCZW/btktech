from django.contrib import admin
from .models import home_poly


class poly_index_01_Admin(admin.ModelAdmin):

    fieldsets = (
        ['CH-Area', {
            'fields': ('poly_index_001', 'poly_index_002', 'poly_index_003', 'poly_index_004', 'poly_index_005', 'poly_index_006'),
        }]
    )


admin.site.register(home_poly)

# Register your models here.

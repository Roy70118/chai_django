from django.contrib import admin
from .models import ChaiVariety, ChaiCertificate, ChaiProducer, ChaiReview

# Register your models here.
# admin.site.register(ChaiVariety)


@admin.register(ChaiVariety)
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ['name', 'data_added', 'type']  # add name into it


class chaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extras = 1


class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number',
                    'issued_date', 'valid_unitil')


admin.site.register(storeAdmin)
admin.site.register(ChaiCertificateAdmin)

# @admin.register(ChaiVariety)
# class ChaiVarietyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image')  # include image

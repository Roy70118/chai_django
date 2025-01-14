from django.contrib import admin
from .models import ChaiVariety, ChaiCertificate, ChaiProducer, ChaiReview
from .models import Store

# Register your models here.
# admin.site.register(ChaiVariety)


@admin.register(ChaiVariety)
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ['name', 'data_added', 'type']  # add name into it


class chaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extras = 1


class storeAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name']
    filter_horizontal = ('chai_varieties',)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_name',
                    'issued_date', 'valid_until')


admin.site.register(Store, storeAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
# admin.site.register(ChaiVariety)
# @admin.register(ChaiVariety)
# class ChaiVarietyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image')  # include image

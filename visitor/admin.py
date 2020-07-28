from django.contrib import admin

from .models import Service, ServiceDetail, SiteConfiguration, Homepage
# Register your models here.

class ServiceDetailInline(admin.TabularInline):
    model = ServiceDetail
    extra = 2

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    can_delete = True
    verbose_name = 'service'
    fields = ['name', 'short_description', 'long_description', 'icon', 'display']

    list_display = ('rank', 'name', 'short_description', 'display')
    inlines = [ServiceDetailInline]

class SiteConfigurationAdmin(admin.ModelAdmin):
    model = SiteConfiguration
    can_delete = False
    verbose_name = 'Site Configuration'

    list_display = ('company_name', 'abbreviation', 'phone_number', 'address')

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


class HomepageAdmin(admin.ModelAdmin):
    model = Homepage
    can_delete = False
    verbose_name = 'Homepage'
    list_display = ('id','our_firm', 'about_us', 'resume')

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


admin.site.register(Service, ServiceAdmin)
admin.site.register(SiteConfiguration, SiteConfigurationAdmin)

admin.site.register(Homepage, HomepageAdmin)

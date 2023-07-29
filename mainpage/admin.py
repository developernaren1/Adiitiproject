from django.contrib import admin
from .models import Query,Domain
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# query
class BrandAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('id','name','email','countrycode','phone','message')

class DamAdmin(ImportExportModelAdmin):
    pass
      

admin.site.register(Query,BrandAdmin)
admin.site.register(Domain,DamAdmin)
# domain add


    



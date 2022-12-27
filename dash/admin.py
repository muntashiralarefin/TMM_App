from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# # Register your models here.
admin.site.register([Tourist, Feedback, Occupation, Education])

admin.site.register([Tour_type, Travel_interest, Travel_season])

admin.site.register([CBT_attraction, CBT_facility, Vacation_package])

# class SexAdmin(ImportExportModelAdmin):
#   pass


# admin.site.register([Sex, SexAdmin])
@admin.register(Sex, District)
class ViewAdmin(ImportExportModelAdmin):
    pass

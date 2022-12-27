from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# # Register your models here.
# admin.site.register([Yes_no,Tourist])

# admin.site.register([Tour_type, Travel_interest, Travel_season])

# admin.site.register([CBT_attraction, CBT_facility, Vacation_package, Satisfaction, Spot])

# class SexAdmin(ImportExportModelAdmin):
#   pass


# admin.site.register([Sex, SexAdmin])
@admin.register(Yes_no, Sex, District, Occupation, Education, Tour_type, Travel_interest, Travel_season, CBT_attraction, CBT_facility, Vacation_package, Satisfaction, Spot)
class ViewAdmin(ImportExportModelAdmin):
    pass

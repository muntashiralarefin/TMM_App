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
@admin.register(Yes_no, Sex, District, Occupation, Education, Tour_type, Travel_interest, Travel_season, CBT_attraction, CBT_facility, Vacation_package, Satisfaction, Spot, Opinion, Expectation_hotel, Reason_food_dissatisfaction, Expectation_street_food, Transport, Transport_manage, Transport_dissatisfaction_reason, Safety_issue, Spot_expectation, Opinion_hawker, Negative_reason_hawker, Clean_suggestion, Recommendation_improve)
class ViewAdmin(ImportExportModelAdmin):
    pass

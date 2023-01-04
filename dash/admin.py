from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# # Register your models here.
# admin.site.register([Yes_no,Tourist])

# Register main models
@admin.register(Tourist,Survey)
class ViewAdmin(ImportExportModelAdmin):
    pass

# Register Choice models
@admin.register(Yes_no, Sex, District, Occupation, Education, Tour_type, Travel_interest, Travel_season, CBT_attraction, CBT_facility, Vacation_package, Satisfaction, Spot, Opinion, Expectation_hotel, Reason_food_dissatisfaction, Expectation_street_food, Transport, Transport_manage, Transport_dissatisfaction_reason, Safety_issue, Spot_expectation, Opinion_hawker, Negative_reason_hawker, Clean_suggestion, Recommendation_improve,CBT_rec1,Tour_operator_dissatisfaction,Tour_operator_recommendation, Room_service_dissatisfaction,Hotel_residence_dissatisfaction, Food_seller_recommendation, Highway_transport_dissatisfaction_reason, Transport_recommendation, Safety_recommendation, Tourist_police_services, Hawker_suggest)
class ViewAdmin(ImportExportModelAdmin):
    pass

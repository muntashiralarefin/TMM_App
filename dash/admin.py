from django.contrib import admin
from .models import *

# # Register your models here.
admin.site.register([Tourist, Feedback, Sex, Occupation, Education])

admin.site.register([District, Tour_type, Travel_interest, Travel_season])

admin.site.register([CBT_attraction, CBT_facility, Vacation_package])


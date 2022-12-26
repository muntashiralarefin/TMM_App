from django.db import models
# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# # Create your models here.
 
### Main
class Sex(models.Model):
    sex = models.CharField('Sex',max_length=15)
    def __str__(self):
        return self.sex

class Occupation(models.Model):
    occupation = models.CharField('Occupation',max_length=15)
    def __str__(self):
        return self.occupation

class Education(models.Model):
    education = models.CharField('Education',max_length=15)
    def __str__(self):
        return self.education

class District(models.Model):
    district = models.CharField('District',max_length=15)
    def __str__(self):
        return self.district

class Spot(models.Model):
    spot = models.CharField('Spot',max_length=15)
    district2 = models.CharField('District',max_length=15)
    def __str__(self):
        return self.spot

class Tour_type(models.Model):
    tour_type = models.CharField('Tour type',max_length=30)
    def __str__(self):
        return self.tour_type

class Travel_interest(models.Model):
    travel_interest = models.CharField('Travel interest',max_length=30)
    def __str__(self):
        return self.travel_interest

class Travel_season(models.Model):
    travel_season = models.CharField('Travel season',max_length=15)
    def __str__(self):
        return self.travel_season

class CBT_attraction(models.Model):
    cbt_attraction = models.CharField('CBT attraction',max_length=15)
    def __str__(self):
        return self.cbt_attraction

class CBT_facility(models.Model):
    cbt_facility = models.CharField('CBT Facility',max_length=15)
    def __str__(self):
        return self.cbt_facility

class Vacation_package(models.Model):
    vacation_package = models.CharField('Vacation package offers',max_length=15)
    def __str__(self):
        return self.vacation_package

#############################################

class Tourist(models.Model):
    a1_name = models.CharField('Tourist name',max_length=30)
    a2_age = models.IntegerField('Age', blank=True)
    a3_gender = models.CharField('Gender',max_length=30, blank=True) ##
    a4_occupation = models.CharField('Occupation',max_length=30, blank=True) ##
    a5_education = models.CharField('Education',max_length=30, blank=True) ##
    a6_mobile = models.CharField('Mobile',max_length=15, blank=True)
    a7_email = models.EmailField('Email address', null=True, blank=True)
    a8_home_dist = models.CharField('District',max_length=30, blank=True) ##
    a9_tour_type = models.CharField('Tour type',max_length=30, blank=True) ##
    a10_travel_interest = models.CharField('Travel interest',max_length=30, blank=True) ##
    a11_season_choices = models.CharField('Season prefer',max_length=30, blank=True) ##
    a12_yearly_travel = models.IntegerField('Average travel day in a year', null=True, blank=True)
    
    def __str__(self):
        return self.a1_name

class Feedback(models.Model):
    b1_visited_dist = models.CharField('District',max_length=30, blank=True) ##
    b21_2_spot = models.CharField('Spot',max_length=30, blank=True) ##
    b2_cbt_known = models.BooleanField('b2_cbt_known')
    b3_cbt_need = models.BooleanField('b3_cbt_need')
    b4_cbt_visit = models.BooleanField('b4_cbt_visit')
    b5_cbt_attraction = models.CharField('Your CBT Attractions',max_length=30, blank=True) ##
    b6_cbt_facility = models.CharField('b6_cbt_facility',max_length=30, blank=True) ##
    b7_vacation_package = models.CharField('b7_vacation_package',max_length=30, blank=True) ##
    b8_tour_operator = models.BooleanField('b8_tour_operator')
    b9_tour_operator_ev = models.IntegerField('b9_tour_operator_ev')
    
    def __str__(self):
        return self.b1_visited_dist




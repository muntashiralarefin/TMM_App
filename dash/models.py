from django.db import models
# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# # Create your models here.
 
### Main
class Yes_no(models.Model):
    yes_no = models.CharField('Yes or No',max_length=10)
    def __str__(self):
        return self.yes_no

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

class Spot(models.Model):
    spot = models.CharField('Vacation package offers',max_length=30)
    def __str__(self):
        return self.spot

class Satisfaction(models.Model):
    satisfaction = models.CharField('Vacation package offers',max_length=30)
    def __str__(self):
        return self.satisfaction

class Opinion(models.Model):
    opinion = models.CharField('Opinion Level',max_length=30)
    def __str__(self):
        return self.opinion

class Expectation_hotel(models.Model):
    expectation_hotel = models.CharField('Expectation hotel',max_length=30)
    def __str__(self):
        return self.expectation_hotel      
      
class Reason_food_dissatisfaction(models.Model):
    reason_food_dissatisfaction = models.CharField('Reason food dissatisfaction',max_length=30)
    def __str__(self):
        return self.reason_food_dissatisfaction       

class Expectation_street_food(models.Model):
    expectation_street_food = models.CharField('Expectation street food',max_length=30)
    def __str__(self):
        return self.expectation_street_food 

class Transport(models.Model):
    transport = models.CharField('Transport',max_length=30)
    def __str__(self):
        return self.transport 

class Transport_manage(models.Model):
    transport_manage = models.CharField('Transport manage',max_length=100)
    def __str__(self):
        return self.transport_manage

class Transport_dissatisfaction_reason(models.Model):
    transport_dissatisfaction_reason = models.CharField('Transport dissatisfaction reason',max_length=200)
    def __str__(self):
        return self.transport_dissatisfaction_reason

class Safety_issue(models.Model):
    safety_issue = models.CharField('Safety issue',max_length=30)
    def __str__(self):
        return self.safety_issue

class Spot_expectation(models.Model):
    spot_expectation = models.CharField('Spot expectation',max_length=30)
    def __str__(self):
        return self.spot_expectation

class Opinion_hawker(models.Model):
    opinion_hawker = models.CharField('Opinion hawker',max_length=200)
    def __str__(self):
        return self.opinion_hawker

class Negative_reason_hawker(models.Model):
    negative_reason_hawker = models.CharField('Negative reason hawker',max_length=200)
    def __str__(self):
        return self.negative_reason_hawker

class Clean_suggestion(models.Model):
    clean_suggestion = models.CharField('Clean suggestion',max_length=30)
    def __str__(self):
        return self.clean_suggestion

class Recommendation_improve(models.Model):
    recommendation_improve = models.CharField('Recommendation improve',max_length=200)
    def __str__(self):
        return self.recommendation_improve

   
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




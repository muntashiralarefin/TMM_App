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
    occupation = models.CharField('Occupation',max_length=30)
    def __str__(self):
        return self.occupation

class Education(models.Model):
    education = models.CharField('Education',max_length=30)
    def __str__(self):
        return self.education

class District(models.Model):
    district = models.CharField('District',max_length=25)
    def __str__(self):
        return self.district

class Spot(models.Model):
    spot = models.CharField('Spot',max_length=50)
    district2 = models.CharField('District',max_length=25)
    def __str__(self):
        return self.spot

class Tour_type(models.Model):
    tour_type = models.CharField('Tour type',max_length=50)
    def __str__(self):
        return self.tour_type

class Travel_interest(models.Model):
    travel_interest = models.CharField('Travel interest',max_length=50)
    def __str__(self):
        return self.travel_interest

class Travel_season(models.Model):
    travel_season = models.CharField('Travel season',max_length=15)
    def __str__(self):
        return self.travel_season

class CBT_attraction(models.Model):
    cbt_attraction = models.CharField('CBT attraction',max_length=50)
    def __str__(self):
        return self.cbt_attraction

class CBT_facility(models.Model):
    cbt_facility = models.CharField('CBT Facility',max_length=50)
    def __str__(self):
        return self.cbt_facility

class Vacation_package(models.Model):
    vacation_package = models.CharField('Vacation package offers',max_length=50)
    def __str__(self):
        return self.vacation_package

class Spot(models.Model):
    spot = models.CharField('Vacation package offers',max_length=50)
    def __str__(self):
        return self.spot

class Satisfaction(models.Model):
    satisfaction = models.CharField('Vacation package offers',max_length=30)
    def __str__(self):
        return self.satisfaction

class Opinion(models.Model):
    opinion = models.CharField('Opinion Level',max_length=200)
    def __str__(self):
        return self.opinion

class Expectation_hotel(models.Model):
    expectation_hotel = models.CharField('Expectation hotel',max_length=200)
    def __str__(self):
        return self.expectation_hotel      
      
class Reason_food_dissatisfaction(models.Model):
    reason_food_dissatisfaction = models.CharField('Reason food dissatisfaction',max_length=200)
    def __str__(self):
        return self.reason_food_dissatisfaction       

class Expectation_street_food(models.Model):
    expectation_street_food = models.CharField('Expectation street food',max_length=200)
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
    safety_issue = models.CharField('Safety issue',max_length=200)
    def __str__(self):
        return self.safety_issue

class Spot_expectation(models.Model):
    spot_expectation = models.CharField('Spot expectation',max_length=100)
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
    clean_suggestion = models.CharField('Clean suggestion',max_length=200)
    def __str__(self):
        return self.clean_suggestion

class Recommendation_improve(models.Model):
    recommendation_improve = models.CharField('Recommendation improve',max_length=200)
    def __str__(self):
        return self.recommendation_improve

class Cbt_Recommendation(models.Model):
    cbt_Recommendation = models.CharField('Recommendations for CBT',max_length=200)
    def __str__(self):
        return self.cbt_Recommendation

class Tour_operator_recommendation(models.Model):
    tour_operator_recommendation = models.CharField('Recommendations for Tour operator',max_length=200)
    def __str__(self):
        return self.tour_operator_recommendation

class Room_service_dissatisfaction(models.Model):
    room_service_dissatisfaction = models.CharField('Reason of room service dissatisfaction',max_length=200)
    def __str__(self):
        return self.room_service_dissatisfaction

class Hotel_residence_dissatisfaction(models.Model):
    hotel_residence_dissatisfaction = models.CharField('Hotel residence dissatisfaction',max_length=200)
    def __str__(self):
        return self.hotel_residence_dissatisfaction

class Food_seller_recommendation(models.Model):
    food_seller_recommendation = models.CharField('Recommendations for food seller',max_length=200)
    def __str__(self):
        return self.food_seller_recommendation

class Safety_recommendation(models.Model):
    safety_recommendation = models.CharField('Recommendations for safety & security',max_length=200)
    def __str__(self):
        return self.safety_recommendation

class Tourist_police_services(models.Model):
    tourist_police_services = models.CharField('Services of tourist police',max_length=200)
    def __str__(self):
        return self.tourist_police_services

class Transport_recommendation(models.Model):
    transport_recommendation = models.CharField('Recommendations for transport',max_length=200)
    def __str__(self):
        return self.transport_recommendation

class Tour_operator_dissatisfaction(models.Model):
    tour_operator_dissatisfaction = models.CharField('Reason behind dissatisfaction on tour operator',max_length=200)
    def __str__(self):
        return self.tour_operator_dissatisfaction
      
#############################################

class Tourist(models.Model):
    a1_name = models.CharField('Tourist name',max_length=30)
    a2_age = models.IntegerField('Age', blank=True)
    a3_gender = models.ForeignKey(Sex , blank=True, null=True, on_delete = models.SET_NULL)
    a4_occupation = models.ForeignKey(Occupation , blank=True, null=True, on_delete = models.SET_NULL)
    a5_education = models.ForeignKey(Education , blank=True, null=True, on_delete = models.SET_NULL)
    a6_mobile = models.CharField('Mobile',max_length=15, blank=True)
    a7_email = models.EmailField('Email address', null=True, blank=True)
    a8_home_dist = models.ForeignKey(District , blank=True, null=True, on_delete = models.SET_NULL)
    a9_tour_type = models.ForeignKey(Tour_type , blank=True, null=True, on_delete = models.SET_NULL)
    a10_travel_interest = models.ForeignKey(Travel_interest , blank=True, null=True, on_delete = models.SET_NULL)
    a11_season_choices = models.ForeignKey(Travel_season , blank=True, null=True, on_delete = models.SET_NULL)
    a12_yearly_travel = models.IntegerField('Average travel day in a year', null=True, blank=True)
    
    def __str__(self):
        return self.a1_name

class Survey(models.Model):
    Yes_No = [('Yes', 'Yes'), ('No', 'No')]
    Sat_level = [("Very satisfied","Very satisfied"), ("Satisfied","Satisfied"), ("Neutral","Neutral"), ("Dissatisfied", "Dissatisfied"), ("Very dissatisfied","Very dissatisfied")]

    name = models.CharField('Name', blank=True, max_length=10)
  
    b1 = models.ForeignKey(District, related_name='visited_dist', blank=True, null=True, on_delete = models.SET_NULL,verbose_name = u'B1_  Select your visited district') # Select your visited district?
  
    b2 = models.ManyToManyField(Spot, blank=True, verbose_name = u'B2_Which tourist spots you visited?') # Which tourist spots you visited?
  
    b3 = models.CharField('B3_Do you know about community based tourism?',choices=Yes_No, blank=True, max_length=10) # Do you know about community based tourism?
  
    b4 = models.CharField('B4_Do you know about community based tourism?', choices=Yes_No, blank=True, max_length=10) #(If b3 is yes) Do you think community based tourism need to be started in here?
  
    b5 = models.CharField('B5_(If b3 is yes) Will you visit any community if community based tourism is started?', choices=Yes_No, blank=True, max_length=10) #(If b3 is yes) Will you visit any community if community based tourism is started?
  
    b6 = models.ManyToManyField(CBT_attraction, blank=True, verbose_name = u'B6_(If b3 is yes) What you want to see during community visit which will attract you?') #(If b3 is yes) What you want to see during community visit which will attract you?
  
    b6_1 = models.CharField("B6_1_(If b3 is yes) Others (What you want to see during community visit which will attract you?)", blank=True, null=True, max_length=500) #(If b3 is yes) Others (What you want to see during community visit which will attract you?)
  
    b7 = models.ManyToManyField(CBT_facility , blank=True, verbose_name=u'B7_(If b3 is yes) Which facilities you expect during community visit?') #(If b3 is yes) Which facilities you expect during community visit?
  
    b7_1 = models.CharField("B7_1_(If b3 is yes) Others (Which facilities you expect during community visit?)", blank=True, null=True, max_length=500) #(If b3 is yes) Others (Which facilities you expect during community visit?)

    b8 = models.ManyToManyField(Cbt_Recommendation, blank=True, verbose_name=u'B8_(If b3 is yes) What are your recommendations to improve community based tourism?') #(If b3 is yes) What are your recommendations to improve community based tourism?

    b8_1 = models.CharField("B8_1_(If b3 is yes) Others (What are your recommendations to improve community based tourism?)", blank=True, null=True, max_length=500)

    c1 = models.CharField('C1_Have you received service from tour operator?', choices=Yes_No, blank=True, max_length=10) # Have you received service from tour operator?

    c2 = models.CharField('C2_(If c1 is yes) How you evaluate the professionalism of tour operators?', choices=Sat_level, blank=True, max_length=20) #(If c1 is yes) How you evaluate the professionalism of tour operators?

    # c3 = models.ManyToManyField(Cbt_Recommendation, blank=True) #(If c2 is dissatisfaction) Reason behind dissatisfaction

    # c3_1 = models.CharField("(If c2 is dissatisfaction) Others (Reason behind dissatisfaction)", blank=True, null=True, max_length=500)

    # c4 = models.ManyToManyField(Vacation_package, blank=True) # As a tourist, what you want in a vacation package?

    # c4_1 = models.CharField("Others (As a tourist, what you want in a vacation package?)", blank=True, null=True, max_length=500)

    # c5 = models.ManyToManyField(Tour_operator_recommendation, blank=True) # What are your recommendations for tour operators?

    # c5_1 = models.CharField(" Others (What are your recommendations for tour operators?)", blank=True, null=True, max_length=500)

    # d1 = models.ForeignKey(Opinion, blank=True, null=True, on_delete = models.SET_NULL) # What is your opinion on the cost of hotel in tourist spots?

    # d2 = models.ForeignKey(Satisfaction, blank=True, null=True, on_delete = models.SET_NULL)

    # d3 = models.ManyToManyField(Room_service_dissatisfaction , blank=True) #(If d2 is dissatisfaction) Reason behind dissatisfation

    # d3_1 = models.CharField(" Others (What are your recommendations for tour operators?)", blank=True, null=True, max_length=500)

    # d4 = models.ForeignKey(Satisfaction, blank=True, null=True, on_delete = models.SET_NULL) # Are you satisfied with hotel residence system in tourist spot?

    # d5 = models.ManyToManyField(Hotel_residence_dissatisfaction , blank=True) #(If d4 is dissatisfaction) Reason behind dissatisfation

    # d5_1 = models.CharField("(If d4 is dissatisfaction) Others (Reason behind dissatisfation)", blank=True, null=True, max_length=500)

    # d6 = models.ManyToManyField(Expectation_hotel , blank=True) # What is your recommendations for hotel service?

    # d6_1 = models.CharField(" Other ( What is your recommendations for hotel service?)", blank=True, null=True, max_length=500)

    # d7 = models.ForeignKey(Satisfaction, related_name='Satis-d7' ,blank=True, null=True, on_delete = models.SET_NULL) #  Are you satisfied with the food of restaurant?

    # d8 = models.ManyToManyField(Reason_food_dissatisfaction , blank=True) # (If d7 is dissatisfaction) Reason behind dissatisfation

    # d8_1 = models.CharField("(If d7 is dissatisfaction) Others (Reason behind dissatisfation)", blank=True, null=True, max_length=500) #(If d7 is dissatisfaction) Others (Reason behind dissatisfation)

        
    def __str__(self):
        return self.name




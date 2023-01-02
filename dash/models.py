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

class Hawker_suggest(models.Model):
    hawker_suggest = models.CharField('Suggests for hawker',max_length=200)
    def __str__(self):
        return self.hawker_suggest

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

class Highway_transport_dissatisfaction_reason(models.Model):
    highway_transport_dissatisfaction_reason = models.CharField('Highway transport dissatisfaction reason',max_length=200)
    def __str__(self):
        return self.highway_transport_dissatisfaction_reason
      
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

################################
class Survey(models.Model):
    Yes_No = [('Yes', 'Yes'), ('No', 'No')]
    Sat_level = [("Very satisfied","Very satisfied"), ("Satisfied","Satisfied"), ("Neutral","Neutral"), ("Dissatisfied", "Dissatisfied"), ("Very dissatisfied","Very dissatisfied")]

    name = models.CharField('Name', blank=True, max_length=10)
  
    b1 = models.ForeignKey(District, related_name='visited_dist', blank=True, null=True, on_delete = models.SET_NULL,verbose_name = u'B1_  Select your visited district') # Select your visited district?
  
    b2 = models.ManyToManyField(Spot, blank=True, verbose_name = u'B2_Which tourist spots you visited?') # Which tourist spots you visited?
  
    b3 = models.CharField('B3_Do you know about community based tourism?',choices=Yes_No, blank=True, max_length=10) # Do you know about community based tourism?
  
    b4 = models.CharField('B4_(If b3 is yes) Do you think community based tourism need to be started in here?', choices=Yes_No, blank=True, max_length=10) #(If b3 is yes) Do you think community based tourism need to be started in here?
  
    b5 = models.CharField('B5_(If b3 is yes) Will you visit any community if community based tourism is started?', choices=Yes_No, blank=True, max_length=10) #(If b3 is yes) Will you visit any community if community based tourism is started?
  
    b6 = models.ManyToManyField(CBT_attraction, blank=True, verbose_name = u'B6_(If b3 is yes) What you want to see during community visit which will attract you?') #(If b3 is yes) What you want to see during community visit which will attract you?
  
    b6_1 = models.CharField("B6_1_(If b3 is yes) Others (What you want to see during community visit which will attract you?)", blank=True, null=True, max_length=500) #(If b3 is yes) Others (What you want to see during community visit which will attract you?)
  
    b7 = models.ManyToManyField(CBT_facility , blank=True, verbose_name=u'B7_(If b3 is yes) Which facilities you expect during community visit?') #(If b3 is yes) Which facilities you expect during community visit?
  
    b7_1 = models.CharField("B7_1_(If b3 is yes) Others (Which facilities you expect during community visit?)", blank=True, null=True, max_length=500) #(If b3 is yes) Others (Which facilities you expect during community visit?)

    b8 = models.ManyToManyField(Cbt_Recommendation, blank=True, verbose_name=u'B8_(If b3 is yes) What are your recommendations to improve community based tourism?') #(If b3 is yes) What are your recommendations to improve community based tourism?

    b8_1 = models.CharField("B8_1_(If b3 is yes) Others (What are your recommendations to improve community based tourism?)", blank=True, null=True, max_length=500)

    c1 = models.CharField('C1_Have you received service from tour operator?', choices=Yes_No, blank=True, max_length=10) # Have you received service from tour operator?

    c2 = models.CharField('C2_(If c1 is yes) How you evaluate the professionalism of tour operators?', choices=Sat_level, blank=True, max_length=20) #(If c1 is yes) How you evaluate the professionalism of tour operators?

    c3 = models.ManyToManyField(Tour_operator_dissatisfaction, blank=True, verbose_name=u'C3_(If c2 is dissatisfaction) Reason behind dissatisfaction') #(If c2 is dissatisfaction) Reason behind dissatisfaction

    c3_1 = models.CharField("C3_1_(If c2 is dissatisfaction) Others (Reason behind dissatisfaction)", blank=True, null=True, max_length=500)

    c4 = models.ManyToManyField(Vacation_package, blank=True, verbose_name=u'C4_As a tourist, what you want in a vacation package?') # As a tourist, what you want in a vacation package?

    c4_1 = models.CharField("C4_1_Others (As a tourist, what you want in a vacation package?)", blank=True, null=True, max_length=500)

    c5 = models.ManyToManyField(Tour_operator_recommendation, blank=True, verbose_name=u'C5_What are your recommendations for tour operators?') # What are your recommendations for tour operators?

    c5_1 = models.CharField("C5_1_ Others (What are your recommendations for tour operators?)", blank=True, null=True, max_length=500)

    d1 = models.ForeignKey(Opinion, blank=True, null=True, on_delete = models.SET_NULL, verbose_name=u'D1_What is your opinion on the cost of hotel in tourist spots?') # What is your opinion on the cost of hotel in tourist spots?

    d2 = models.CharField('D2_Are you satisfied with hotel room service?', blank=True, max_length=30, choices=Sat_level)

    d3 = models.ManyToManyField(Room_service_dissatisfaction , blank=True, verbose_name=u'D3_(If d2 is dissatisfaction) Reason behind dissatisfation') #(If d2 is dissatisfaction) Reason behind dissatisfation

    d3_1 = models.CharField("D3_1_Others (What are your recommendations for tour operators?)", blank=True, null=True, max_length=500)

    d4 = models.CharField('D4_Are you satisfied with hotel residence system in tourist spot?', blank=True, choices=Sat_level, max_length=500) # Are you satisfied with hotel residence system in tourist spot?

    d5 = models.ManyToManyField(Hotel_residence_dissatisfaction , blank=True, verbose_name=u'D5_(If d4 is dissatisfaction) Reason behind dissatisfation') #(If d4 is dissatisfaction) Reason behind dissatisfation

    d5_1 = models.CharField("D5_1_(If d4 is dissatisfaction) Others (Reason behind dissatisfation)", blank=True, null=True, max_length=500)

    d6 = models.ManyToManyField(Expectation_hotel , blank=True, verbose_name=u'D6_What is your recommendations for hotel service?') # What is your recommendations for hotel service?

    d6_1 = models.CharField("D6_1_Other ( What is your recommendations for hotel service?)", blank=True, null=True, max_length=500)

    d7 = models.CharField('D7_Are you satisfied with the food of restaurant?', blank=True, max_length=30, choices=Sat_level) #  Are you satisfied with the food of restaurant?

    d8 = models.ManyToManyField(Reason_food_dissatisfaction , blank=True, verbose_name=u'D8_(If d7 is dissatisfaction) Reason behind dissatisfation') # (If d7 is dissatisfaction) Reason behind dissatisfation

    d8_1 = models.CharField('D8_1_(If d7 is dissatisfaction) Others (Reason behind dissatisfation)', blank=True, null=True, max_length=500) #(If d7 is dissatisfaction) Others (Reason behind dissatisfation)

    d9 = models.CharField('D9_ Do you like street food of tourist spots?', blank=True, max_length=10, choices=Yes_No) # Do you like street food of tourist spots?

    d10 = models.ManyToManyField( Expectation_street_food, blank=True, verbose_name=u'D10_ What you expect from street food sellers during food serving?') # What you expect from street food sellers during food serving?
  
    d10_1 = models.CharField('D10_1_ Other expectations on street food', blank=True, null=True, max_length=500) # Other expectations on street food
  
    d11 = models.ManyToManyField( Food_seller_recommendation, blank=True, verbose_name=u'D11_ What is your recommendation to increase the skill of food seller?') # What is your recommendation to increase the skill of food seller?
  
    d11_1 = models.CharField('D11_1_ Others (What is your recommendation to increase the skill of food seller?)', blank=True, null=True, max_length=500) # Others (What is your recommendation to increase the skill of food seller?)
    
    e1 = models.ManyToManyField( Transport, blank=True, verbose_name=u'E1_ What transport you used to travel?') # What transport you used to travel?
  
    e1_1 = models.CharField('E1_1_ Mention other transport', blank=True, null=True, max_length=500) # Mention other transport
  
    e2 = models.CharField('E2_Have you managed your transport by own to come here?', blank=True, max_length=10, choices=Yes_No) # Have you managed your transport by own to come here?
  
    e3 = models.ForeignKey( Transport_manage, blank=True, null=True, on_delete = models.SET_NULL, verbose_name=u'E3_ How you have managed transport?') #  How you have managed transport?
  
    e3_1 = models.CharField('E3_1_ Mention other process', blank=True, null=True, max_length=500) # Mention other process
  
    e4 = models.CharField('E4_ Are you satisfied with the highway transport system?', blank=True, max_length=200, choices=Sat_level) #  Are you satisfied with the highway transport system?
  
    e5 = models.ManyToManyField( Highway_transport_dissatisfaction_reason, blank=True, verbose_name=u'E5_(If e4 is dissatisfaction) Reason behind dissatisfation') #(If e4 is dissatisfaction) Reason behind dissatisfation
  
    e5_1 = models.CharField('E5_1_(If e4 is dissatisfaction) Others (Reason behind dissatisfation)', blank=True, null=True, max_length=500) #(If e4 is dissatisfaction) Others (Reason behind dissatisfation)
  
    e6 = models.CharField('E6_Are you satisfied with the internal transport (tomtom/riksha) of this area?', blank=True, max_length=30, choices=Sat_level) #  Are you satisfied with the internal transport (tomtom/riksha) of this area?
  
    e7 = models.ManyToManyField( Transport_dissatisfaction_reason, blank=True, verbose_name=u'E7_(If e6 is dissatisfaction) Reason behind dissatisfation') #(If e6 is dissatisfaction) Reason behind dissatisfation
  
    e7_1 = models.CharField('E7_1_(If e6 is dissatisfaction) Others (Reason behind dissatisfation)', blank=True, null=True, max_length=500) #(If e6 is dissatisfaction) Others (Reason behind dissatisfation)
  
    e8 = models.ManyToManyField( Transport_recommendation, blank=True, verbose_name=u'E8_ What is your recommendation to increase the skill of tomtom/riksha driver?') # What is your recommendation to increase the skill of tomtom/riksha driver?
  
    e8_1 = models.CharField('E8_1_ Others (What is your recommendation to increase the skill of tomtom/riksha driver?)', blank=True, null=True, max_length=500) # Others (What is your recommendation to increase the skill of tomtom/riksha driver?)
    
    f1 = models.CharField('F1_ Do you like midnight travelling?', blank=True, max_length=10, choices=Yes_No) #  Do you like midnight travelling?
  
    f2 = models.CharField('F2_ Do you think this place is safe for midnight visiting?', blank=True, max_length=10, choices=Yes_No) #  Do you think this place is safe for midnight visiting?
  
    f3 = models.CharField('F3_Are you satisfied the security of this place?', blank=True, max_length=30, choices=Sat_level) #  Are you satisfied the security of this place?
  
    f4 = models.CharField('F4_ Have you ever harrassed by local people?', blank=True, max_length=10, choices=Yes_No) #  Have you ever harrassed by local people?
  
    f5 = models.CharField('F5_ Have you ever faced any problem during visiting tourist spot?', blank=True, max_length=10, choices=Yes_No) # Have you ever faced any problem during visiting tourist spot? 
  
    f6 = models.ManyToManyField( Safety_issue, blank=True, verbose_name=u'F6_(If f4 or f5 yes) What type of problems you faced?') #(If f4 or f5 yes) What type of problems you faced?
  
    f6_1 = models.CharField('F6_1_ Other problems', blank=True, null=True, max_length=500) # Other problems
  
    f7 = models.ManyToManyField( Safety_recommendation, blank=True, verbose_name=u'F7_ How do you think these problem can be solved?') # How do you think these problem can be solved?
  
    f7_1 = models.CharField('F7_1_ Others (How do you think these problem can be solved?)', blank=True, null=True, max_length=500) # Others (How do you think these problem can be solved?)
    
    h1 = models.CharField('H1_ Do you know about the activity of tourist police?', blank=True, max_length=10, choices=Yes_No) #  Do you know about the activity of tourist police?
  
    h2 = models.CharField('H2_ Do you ever received any service from tourist police?', blank=True, max_length=10, choices=Yes_No) #  Do you ever received any service from tourist police?
  
    h3 = models.ManyToManyField( Tourist_police_services, blank=True, verbose_name=u'H3_(If h2 is yes) What type of service you received?') #(If h2 is yes) What type of service you received?
  
    h3_1 = models.CharField('', blank=True, null=True, max_length=500) #
    
    g1 = models.ForeignKey( Opinion_hawker, blank=True, null=True, on_delete = models.SET_NULL, verbose_name=u'G1_What is your opinion on presence of hawker in tourist spot?') #  What is your opinion on presence of hawker in tourist spot?
  
    g2 = models.ManyToManyField( Negative_reason_hawker, blank=True, verbose_name=u'G2_(If g1 is negative) Reasons behind negative opinion') #(If g1 is negative) Reasons behind negative opinion
  
    g2_1 = models.CharField('G2_1_ Other (Reasons behind negative opinion)', blank=True, null=True, max_length=500) # Other (Reasons behind negative opinion)
  
    g3 = models.CharField('G3_ Do you think rehabilitation of hawkers is necessary?', blank=True, max_length=10, choices=Yes_No) #  Do you think rehabilitation of hawkers is necessary?
  
    g4 = models.ManyToManyField( Hawker_suggest, blank=True, verbose_name=u'G4_ What are your recommendations to increase the skill of hawkers?') # What are your recommendations to increase the skill of hawkers?
  
    g4_1 = models.CharField('G4_1_ Others ( What are your recommendations to increase the skill of hawkers?)', blank=True, null=True, max_length=500) # Others recommendations
    
    i1 = models.CharField('I1_Do you think this tourist spot is cleaned enough?', blank=True, max_length=10, choices=Yes_No) #  Do you think this tourist spot is cleaned enough?
  
    i2 = models.CharField('I2_Do you think you are cooperating to clean this area?', blank=True, max_length=10, choices=Yes_No) #  Do you think you are cooperating to clean this area?
  
    i3 = models.ManyToManyField(Clean_suggestion, blank=True, verbose_name=u'I3_ What is your recemmendation to clean this area?') # What is your recemmendation to clean this area?
  
    i3_1 = models.CharField('I3_1_ Others', blank=True, null=True, max_length=500) # Others
    
    k1 = models.ManyToManyField(Spot_expectation , blank=True, verbose_name=u'K1_What you expect from tourist spot?') #What you expect from tourist spot?
  
    k1_1 = models.CharField('K1_1_ Others ( What you expect from tourist spot?)', blank=True, null=True, max_length=500) # Others expectation
  
    k2 = models.ManyToManyField(Recommendation_improve, blank=True, verbose_name=u'K2_How tourism sector can be developed according to you?') #
  
    k2_1 = models.CharField('K2_1_ Other ( How tourism sector can be developed according to you?)', blank=True, null=True, max_length=500) # Other recommendations

        
    def __str__(self):
        return self.name




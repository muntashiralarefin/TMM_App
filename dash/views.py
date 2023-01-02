from django.shortcuts import render
from .models import *
from django.db.models import Count
import pandas as pd
import plotly.express as px


def home(request):
  data = Survey.objects.all().values()
  # Both model need >>>data = Survey.objects.all().values()
  #For option linked with other model based analysis use analysis3 like below:
  #Example:>>> result = analysis3('b6', CBT_attraction, 'cbt_attraction')
  # For Yes_no or Satisfaction model use analysis2
  # Return [level, percentage, count, Total ]
  def analysis2(field): # Return [level, percentage, count, Total ]
    d3_level = data.values_list(field, flat=True).distinct() # Find category level
    search_type = 'contains'
    filter = field + '__' + search_type
    # # Count by level list
    countres = []
    level = []
    for i in d3_level:
      if i != '':
        level.append(i)
    for i in level:
      d2 = data.filter(**{ filter: i }).count()  ## Change filter variable
      countres.append(d2)
      
    response = sum(countres)
    percentage = []
    for tot in countres:
      if response>0:
        cal = round((tot/response)*100, 0)
        percentage.append(cal)
    return [level, percentage, countres, response]
  #end analysis2 funtion
    # Return [level, percentage, count, Total ]

  #end analysis2 funtion
  # b3_r = analysis3('b6', CBT_attraction, cbt_attraction)
  # print(b3_r[0], b3_r[1])
  # model = data
  # d = analysis2('b6')
  # print(d)

  def analysis3(field, opt_model, opt_field): #Example:>>> result = analysis3('b6', CBT_attraction, 'cbt_attraction')
    df = opt_model.objects.all()
    qlevel = df.values_list(opt_field, flat=True).distinct()
    level = []
    for i in qlevel:
      level.append(i)
    elevel = data.values_list(field, flat=True).distinct()
    level_num_list = []
    for i in elevel:
      level_num_list.append(str(i))
  
    countres = []
    for i in level_num_list:
        d2 = data.filter(**{ field: i }).count()  ## Change filter variable
        countres.append(d2)
    
    percentage = []
    total = data.count()
    for i in countres:
      percentage.append((i/total)*100)
    return [level, percentage, countres, total]

  # ###############################################################
  rr = analysis2('b3')
  print('Result B3: ',rr)
  r = analysis3('b6', CBT_attraction, 'cbt_attraction')
  print('Result B6: ',r)
  # fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

  return render(request, 'dash/home.html', {
    
  })

def survey(request):

  return render(request, 'dash/survey.html', {})

def story(request):
    return render(request, 'dash/story.html', {})

def about(request):
    return render(request, 'dash/about.html', {})

# def about(request):
#     return render(request, 'dash2/index.html', {})

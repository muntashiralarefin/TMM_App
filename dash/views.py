from django.shortcuts import render
from .models import Survey
#import pandas as pd


def home(request):
  data = Survey.objects.all().values()
  
  # Return [level, percentage, count, Total ]
  def analysis2(field): # Return [level, percentage, count, Total ]
    d3_level = data.values_list(field, flat=True).distinct() # Find category level
    search_type = 'contains'
    filter = field + '__' + search_type
    # # Count by level list
    countres = []
    level = []
    for i in d3_level:
      d2 = data.filter(**{ filter: i }).count()  ## Change filter variable
      countres.append(d2)
      level.append(i)
    response = sum(countres)
    percentage = []
    for tot in countres:
      if response>0:
        cal = round((tot/response)*100, 0)
        percentage.append(cal)
    return [level, percentage, countres, response]
  #end analysis2 funtion

  b3_r = analysis2('b3')
  print(b3_r[0], b3_r[1])


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

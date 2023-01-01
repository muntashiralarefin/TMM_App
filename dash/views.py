from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dash/home.html', {})

def survey(request):
    return render(request, 'dash/survey.html', {})

def story(request):
    return render(request, 'dash/story.html', {})

def about(request):
    return render(request, 'dash/about.html', {})

# def about(request):
#     return render(request, 'dash2/index.html', {})

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='sign-in'),
    path('', include('dash.urls')),
]

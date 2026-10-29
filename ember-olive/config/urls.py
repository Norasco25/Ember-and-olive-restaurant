from django.contrib import admin
from django.urls import path
from restaurant.views import home,reserve
urlpatterns=[path('',home),path('reserve/',reserve),path('admin/',admin.site.urls)]

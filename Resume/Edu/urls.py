from django.urls import path
from Edu import views
urlpatterns = [

    path('',views.skill,name="skill")
]

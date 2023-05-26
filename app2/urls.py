from django.urls import path
from app2.views import*
app_name='two'
urlpatterns=[
    path('virat/',virat,name='virat')
]
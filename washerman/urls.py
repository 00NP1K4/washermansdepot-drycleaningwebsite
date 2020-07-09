from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('commercial', views.commercial, name='commercial'),
    path('drycleaning', views.drycleaning, name='drycleaning'),
    path('laundromat', views.laundromat, name='laundromat'),
    path('schedule', views.schedule, name='schedule'),
    path('prices', views.price, name='price'),
    path('contact', views.contact, name='contact'),
]
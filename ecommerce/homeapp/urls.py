from django.urls import path
from . import views
from django.conf.urls import include

app_name='homeapp'
urlpatterns=[
    path('',views.homeapp),
    path('',include('authapp.urls')),
]